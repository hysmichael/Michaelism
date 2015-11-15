 # -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

WORD_TYPE_COLER_CODING = {
    'noun'                          : 'primary',
    'verb (used with object)'       : 'warning',
    'verb (used without object)'    : 'warning',
    'verb phrases'                  : 'danger',
    'adjective'                     : 'success',
    'adverb'                        : 'info',
}

class WordDefinition:
    def __init__(self, dom):
        self.number = int(dom.find(class_='def-number').string[:-1])
        self.content = dom.find(class_='def-content').get_text(' ', strip=True)

class DictionaryWord:
    def __init__(self, word):
        request_url = 'http://dictionary.reference.com/browse/%s?s=t' % word
        response = requests.get(request_url)
        self.dom = BeautifulSoup(response.content, 'html.parser')

    def entry(self):
        return self.dom.find(class_='head-entry').span.string

    def difficulty_index(self):
        return self.dom.find(id='difficulty-box')['data-difficulty']

    def definitions(self):
        def_typesets = self.dom.select('.source-luna .def-pbk')
        all_definitions = []
        for typeset in def_typesets:
            word_type = typeset.header.span.string.lower()
            if word_type == 'idioms': break
            color = WORD_TYPE_COLER_CODING.get(word_type, 'default')
            defs = typeset.find_all(class_='def-set')
            all_definitions.append((word_type, color, map(lambda w: WordDefinition(w), defs)))
        return all_definitions
