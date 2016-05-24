from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Reset
from floppyforms.__future__.models import ModelForm
import floppyforms.__future__ as forms

from . import models


class AnnotationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnotationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'annotations:create'
        self.helper.layout = Layout(
            'text',
            'text_object',
            'text_start_index',
            'text_end_index',
            'user',
            FormActions(
                Submit('save', 'Annotate'),
                Reset('reset', 'Nevermind'),
            )
        )

    class Meta:
        model = models.Annotation
        fields = [
            'text',
            'text_object',
            'text_start_index',
            'text_end_index',
            'user',
        ]
        # `text` is the only field we actually want rendered to the user
        widgets = {
            'text_object': forms.HiddenInput(),
            # 'text_start_index': forms.HiddenInput(),
            # 'text_end_index': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }
