from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from edc_base.views.edc_base_view_mixin import EdcBaseViewMixin


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'example/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
