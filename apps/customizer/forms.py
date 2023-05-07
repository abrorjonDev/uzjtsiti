from django import forms
from ckeditor.widgets import CKEditorWidget

from customizer.models import News


class NewsForm(forms.ModelForm):
    article = forms.CharField(widget=CKEditorWidget()) # config_name='essential'

    class Meta:
        model = News
        fields = "__all__"
