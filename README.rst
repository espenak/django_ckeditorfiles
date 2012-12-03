CKEditor bundled as a Django app.


Install
=======

::

    $ pip install django_ckeditorfiles


Setup
=====

Add ``'ckeditorfiles'`` and ``'django.contrib.staticfiles'`` to
``INSTALLED_APPS``.


Verify install
==============
Start the Django development server (runserver), and open
http://localhost:8000/static/ckeditorfiles/samples/index.html. You should get
the CKEditor examples page.


CKEditor version
================
See ``static/ckeditorfiles/CHANGES.md``.


.. _ckeditorjs:

ckeditor.js
===========

The entire source code of CKEditor is in ``static/ckeditorfiles/``. This means
that you can include the sources in your templates using::

    {% load staticfiles %}

    <script type="text/javascript"
        src="{% static "ckeditorfiles/ckeditor.js" %}"></script>

(you do not need to do this if you use the CKEditorWidget)


ckeditorfiles.widgets.CKEditorWidget
====================================

CKEditorWidget is a subclass of ``django.forms.widgets.Textarea``. It
automatically includes ``ckeditor.js``, and adds::

    <script type="text/javascript">
        CKEDITOR.replace(id, config);
    </script>

after the textarea. ``id`` is the id of the textarea, and ``config`` is
the ``config`` parameter to the constructor of the widget, encoded as JSON.


Example
-------

In your ``forms.py`` or wherever you define your forms:: 

    from django import forms
    from ckeditorfiles.widgets import CKEditorWidget

    class PageForm(forms.Form):
        body = forms.CharField(widget=CKEditorWidget())


In the template rendering the form (we assume you name your form ``form`` in the template context)::

    {{ form.media }}
    {{ form.as_p }}

NOTE: ``form.as_p`` is just an example. The widget also works with
django-crispy-forms, and ``form.as_ul``. The important part is ``form.media``,
because the ckeditor javascript will not be loaded without it. Alternatively, you can
add ckeditor.js manually (see: ckeditorjs_).


The config parameter to ``CKEditorWidget`` is the config parameter for
``CKEDITOR.replace(...)``. See:
http://docs.cksource.com/CKEditor_3.x/Developers_Guide/Setting_Configurations.



Configuration examples
----------------------

Simple toolbar with bold, italic and show source (with show source in its own box)::

    from django import forms
    from ckeditorfiles.widgets import CKEditorWidget

    class PageForm(forms.Form):
        body = forms.CharField(
            widget=CKEditorWidget(config={
                'toolbar': [{
                    'name': 'basic',
                    'items': [ 'Bold', 'Italic']
                }, {
                    'name': 'source',
                    'items': [ 'Source']
                }]
            })
        ))


A more complex toolbar, suitable to simple editors, like comments::

    from django import forms
    from ckeditorfiles.widgets import CKEditorWidget

    class PageForm(forms.Form):
        body = forms.CharField(
            widget=CKEditorWidget(config={
                #'contentsCss': settings.STATIC_URL + 'my_theme/ckeditor.css', # CSS for the body (see static/ckeditorfiles/contents.css for the default)
                'format_tags': 'p;h4', # Only "normal" and "h4" to avoid large headings in the comments
                'toolbar': [{
                    'name': 'format',
                    'items': ['Format']
                }, {
                    'name': 'basic',
                    'items': ['Bold', 'Italic', '-', 'RemoveFormat']
                }, {
                    'name': 'links',
                    'items': ['Link', 'Unlink']
                }, {
                    'name': 'listandindent',
                    'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']
                }, {
                    'name': 'paste',
                    'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']
                }, {
                    'name': 'tools',
                    'items': ['Maximize']
                }]
            })
            )
            
        ))


The full default toolbar (good as a source of button-names for your own config)::

    class PageForm(forms.Form):
        body = forms.CharField(
            widget=CKEditorWidget(config={
                'toolbar': [
                    {
                        'name': 'document',
                        'groups': [ 'mode', 'document', 'doctools' ],
                        'items': [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ]
                    },
                    {
                        'name': 'clipboard',
                        'groups': [ 'clipboard', 'undo' ],
                        'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ]
                    },
                    {
                        'name': 'editing',
                        'groups': [ 'find', 'selection', 'spellchecker' ],
                        'items': [ 'Find', 'Replace', '-', 'SelectAll' ]
                    },
                    {
                        'name': 'forms',
                        'items': [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ]
                    },
                    '/', # Linebreak
                    {
                        'name': 'basicstyles',
                        'groups': [ 'basicstyles', 'cleanup' ],
                        'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ]
                    },
                    {
                        'name': 'paragraph',
                        'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ],
                        'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl' ]
                    },
                    {
                        'name': 'links',
                        'items': [ 'Link', 'Unlink', 'Anchor' ]
                    },
                    {
                        'name': 'insert',
                        'items': [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ]
                    },
                    '/', # Linebreak
                    {
                        'name': 'styles',
                        'items': [ 'Styles', 'Format', 'Font', 'FontSize' ]
                    },
                    {
                        'name': 'colors',
                        'items': [ 'TextColor', 'BGColor' ]
                    },
                    {
                        'name': 'tools',
                        'items': [ 'Maximize', 'ShowBlocks' ]
                    },
                    {
                        'name': 'others',
                        'items': [ '-' ]
                    },
                    {
                        'name': 'about',
                        'items': [ 'About' ]
                    }
                ],
                'toolbarGroups': [
                        {'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ]},
                        {'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ]},
                        {'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker' ]},
                        {'name': 'forms'},
                        '/',
                        {'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ]},
                        {'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ]},
                        {'name': 'links'},
                        {'name': 'insert'},
                        '/',
                        {'name': 'styles'},
                        {'name': 'colors'},
                        {'name': 'tools'},
                        {'name': 'others'},
                        {'name': 'about'}
                ]
            })
        ))



Subclass CKEditorWidget
-----------------------

You can create your own CKEditor configurations as re-usable classes by
subclassing CKEditorWidget and provide defaults in the ``default_config`` class
attribute::

    from ckeditorfiles.widgets import CKEditorWidget

    class MyCKEditorWidget(CKEditorWidget):
        default_config = {'toolbar': 'Basic',
                          'height': '300px'}

The ``default_config`` class attribute provides defaults that can be overridden
with ``config`` parameter for __init__, so you could
override the height-config of ``MyCKEditorWidget`` like this::

    widget = MyCKEditorWidget(config={'height': '100px'})
