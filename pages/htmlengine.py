from django.templatetags.static import static
from django.template.defaultfilters import linebreaks
import re

def render_essay_introduction(essay, limit):
    value = linebreaks(essay.body)
    paragraphes = re.findall('<p>.+?</p>', value)
    count = 0
    if (essay.language.name == 'Chinese'):  limit = int(limit * 0.5)
    if (essay.language.name == 'Japanese'): limit = int(limit * 0.5)
    countMax = limit
    outputStr = ''
    for index, text in enumerate(paragraphes):
        if (count + len(text) <= countMax):
            outputStr += text
            count += len(text)
        else:
            break
    if (index < len(paragraphes)):
        # truncate by words #
        truncateText = paragraphes[index][:countMax - count].rsplit(' ', 1)[0] + ' ...'
        
        # complete opened html tags #
        tags = re.findall('</*(.+?)>', truncateText)
        stack = []
        for tag in tags:
            if len(stack) > 0 and stack[-1] == tag:
                stack.pop()
            else:
                stack.append(tag)
        for tag in reversed(stack):
            truncateText += '</%s>' % tag
        
        # append trucated text #
        outputStr += truncateText
    return outputStr


def render_html_body(essay):
    text = essay.body

    # scan [IMG] tag and replace with proper image url
    text = re.sub('\[\s*IMG\s*\*=\s*([\w-]+.(jpg|png))\s*([\w%]*)\s*\]', image_tag_render(essay.slug), text)
    
    # scan [REF] tag and replace with proper numbering
    reflist = []
    text = re.sub('\[\s*REF\s*\*=\s*([^\]]+)\s*\]', reference_tag_render(reflist), text)
    text += generate_reference_list(reflist)

    # scan [CODE] tag and generate a properly formatted code snippet
    text = re.sub('\[ *CODE *\*= *([\w]+) *([\w]*) *BEGIN\*(.+?)\*END *\]', code_snippet_render, text, flags=re.DOTALL)

    return text

def image_tag_render(slug):
    def path_replace(matchobj):
        filename = matchobj.group(1)
        width = matchobj.group(3)
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


