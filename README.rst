CKEditor bundled as a Django app.


Install
=======

::

    $ pip install ckeditorfiles


Setup
=====

Add ``'ckeditorfiles'`` and ``'django.contrib.staticfiles'`` to
``INSTALLED_APPS``.


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

:: 

    from django import forms
    from ckeditorfiles.widgets import CKEditorWidget
    from models import Page

    class PageForm(forms.ModelForm):
        body = forms.CharField(widget=CKEditorWidget(config={'toolbar': 'Basic',
                                                             'height': '300px'}))
        class Meta:
            model = Page


The config parameter to CKEditorWidget is the config parameter for
``CKEDITOR.replace(...)``. See:
http://docs.cksource.com/CKEditor_3.x/Developers_Guide/Setting_Configurations.


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
