import json
from django.conf import settings
from django.forms.utils import flatatt
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django import forms


class CKEditorWidget(Textarea):
    default_config = {}
    def __init__(self, attrs=None, config={}):
        self.config = self.__class__.default_config.copy()
        self.config.update(config)
        super(CKEditorWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        cssclass = 'ckeditorwidget'
        if 'class' in attrs:
            cssclass += ' ' + attrs['class']
        attrs['class'] = cssclass
        final_attrs = self.build_attrs(attrs, name=name)
        script = ('\n<script type="text/javascript">\n'
                  'CKEDITOR.replace("{id}", {config});\n'
                  '</script>\n').format(id=attrs['id'],
                                        config=json.dumps(self.config, indent=2))
        return mark_safe(u'<textarea{attrs}>{value}</textarea>{script}'.format(attrs=flatatt(final_attrs),
                                                                       value=conditional_escape(force_unicode(value)),
                                                                       script=script))

    def _media(self):
        js = [settings.STATIC_URL + 'ckeditorfiles/ckeditor.js']
        return forms.Media(js=js)
    media = property(_media)
