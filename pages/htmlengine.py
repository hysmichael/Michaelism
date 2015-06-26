from django.templatetags.static import static
from django.conf import settings

import codecs
import re

def render_html_body(essay):
    filename = '%s/blogs/%s.esy' % (settings.BASE_DIR, essay.slug) 
    with codecs.open(filename, "r", "utf-8") as essay_content:
        text = essay_content.read()

    # scan [IMG] tag and replace with proper image url
    text = re.sub(r'\[\s*IMG\s*\*=\s*([\w-]+.(jpg|png))\s*([\w%]*)\s*\]', image_tag_render(essay.slug), text)
    
    # scan [REF] tag and replace with proper numbering
    reflist = []
    text = re.sub(r'\[\s*REF\s*\*=\s*([^\]]+)\s*\]', reference_tag_render(reflist), text)
    text += generate_reference_list(reflist)

    # scan [CODE] tag and generate a properly formatted code snippet
    text = re.sub(r'\[\s*CODE\s*\*=\s*([\w]+)\s*([\w]*)\s*BEGIN\*(.+?)\*END\s*\]', code_snippet_render, text, flags=re.DOTALL)

    return text

def image_tag_render(slug):
    def path_replace(matchobj):
        filename = matchobj.group(1)
        width = matchobj.group(3)
        if not width:       # default value for unspecified width
            width = '100%'
        path = 'blog-image/%s/%s' % (slug, filename)
        url  = static(path)
        return '<img class="inline-image" src="%s" style="max-width:%s">' % (url, width)
    return path_replace

def reference_tag_render(reflist): 
    def number_replace(matchobj):
        refname = matchobj.group(1)
        reflist.append(refname)
        return '<a class="ref-number" data-toggle="tooltip" title="%s"><sup>%d</sup></a>' % (refname, len(reflist))
    return number_replace

def generate_reference_list(reflist):
    if len(reflist) == 0:
        return ''

    refkey = {}
    for i in range(0, len(reflist)):
        ref = reflist[i]
        if ref not in refkey:
            refkey[ref] = i
    output = '<div class="reference"><h4>References</h4><ol>'
    for i in range(0, len(reflist)):
        ref = reflist[i]
        if refkey[ref] != i:
            ref = u'same as <p class="number">%d</p>' % (refkey[ref] + 1)
        output += '<li>%s</li>' % ref
    output += '</ol></div>'
    return output

def code_snippet_render(matchobj):
    language = matchobj.group(1)
    arg = matchobj.group(2)
    snippet = matchobj.group(3).split('\r\n')
    while (snippet[0] == u''):
        del snippet[0]
    while (snippet[-1] == u''):
        del snippet[-1]
    snippet = map(lambda line: '<code class="language-%s">%s</code>' % (language, line), snippet)
    if arg == '':
        output = '\r\n'.join(snippet)
    elif arg == 'block':
        output = '<pre>%s</pre>' % ('\r\n'.join(snippet))
    return output


