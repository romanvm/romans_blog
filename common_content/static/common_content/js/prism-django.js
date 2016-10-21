// Django/Jinja2 syntax definition for Prism.js <http://prismjs.com> syntax highlighter.
// Mostly it works OK but can paint code incorrectly on complex html/template tag combinations.

var django_template = {
  'property': {
    pattern: /(?:{{|{%)[\w\W]*?(?:%}|}})/g,
    inside: {
      'string': {
        pattern: /("|')(?:\\\\|\\?[^\\\r\n])*?\1/,
        greedy: true
      },
      'keyword': /\b(?:\||load|verbatim|widthratio|ssi|firstof|for|url|ifchanged|csrf_token|lorem|ifnotequal|autoescape|now|templatetag|debug|cycle|ifequal|regroup|comment|filter|if|spaceless|with|extends|block|include|else|empty|endif|endfor|as|endblock|endautoescape|endverbatim|trans|True|False|None|in|is|static|macro|endmacro|call|endcall|endfilter|set|endset)\b/,
      'operator' : /[-+=]=?|!=|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]|\b(?:or|and|not)\b/,
      'function': /\b(?:abs|add|addslashes|attr|batch|callable|capfirst|capitalize|center|count|cut|d|date|default|default_if_none|defined|dictsort|dictsortreversed|divisibleby|e|equalto|escape|escaped|escapejs|even|filesizeformat|first|float|floatformat|force_escape|forceescape|format|get_digit|groupby|indent|int|iriencode|iterable|join|last|length|length_is|linebreaks|linebreaksbr|linenumbers|list|ljust|lower|make_list|map|mapping|none|number|odd|phone2numeric|pluralize|pprint|random|reject|rejectattr|removetags|replace|reverse|rjust|round|safe|safeseq|sameas|select|selectattr|sequence|slice|slugify|sort|string|stringformat|striptags|sum|time|timesince|timeuntil|title|trim|truncate|truncatechars|truncatechars_html|truncatewords|truncatewords_html|undefined|unordered_list|upper|urlencode|urlize|urlizetrunc|wordcount|wordwrap|xmlattr|yesno)\b/,
      'important': /\b-?\d+(?:\.\d+)?\b/,
      'variable': /\b\w+?\b/,
      'punctuation' : /[[\];(),.:]/
    }
  },
};

Prism.languages.django = Prism.languages.extend('markup', {'comment': /(?:<!--|{#)[\w\W]*?(?:#}|-->)/});
// Updated html tag pattern to allow template tags inside html tags
Prism.languages.django.tag.pattern = /<\/?(?!\d)[^\s>\/=$<]+(?:\s+[^\s>\/=]+(?:=(?:("|')(?:\\\1|\\?(?!\1)[\w\W])*\1|[^>=]+))?)*\s*\/?>/i;
Prism.languages.insertBefore('django', 'entity', django_template);
Prism.languages.insertBefore('inside', 'tag', django_template, Prism.languages.django.tag);

if (Prism.languages.javascript) {
  // Combine js code and template tags painting inside <script> blocks
  Prism.languages.insertBefore('inside', 'string', django_template, Prism.languages.django.script);
  Prism.languages.django.script.inside.string.inside = django;
}
if (Prism.languages.css) {
  // Combine css code and template tags painting inside <style> blocks
  Prism.languages.insertBefore('inside', 'atrule', {'tag': django_template.property}, Prism.languages.django.style);
  Prism.languages.django.style.inside.string.inside = django_template;
}

// Add an Jinja2 alias
Prism.languages.jinja2 = Prism.languages.django;
