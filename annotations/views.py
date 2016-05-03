from django.views.generic import CreateView

from braces.views import LoginRequiredMixin

from . import forms, models
from manifestos.mixins import SuccessMessageMixin


class AnnotationCreateView(LoginRequiredMixin, SuccessMessageMixin,
                           CreateView):
    template_name = 'manifestos/manifesto_detail.html'
    form_class = forms.AnnotationForm
    model = models.Annotation
    success_msg = 'Annotation saved.'

    def get_success_url(self):
        return self.object.text_object.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(self, AnnotationCreateView).form_valid(form)
