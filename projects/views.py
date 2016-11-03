from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import Project


class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'description', 'max_members', 'difficulty', 'image']
    success_url = reverse_lazy('project_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'description', 'max_members', 'difficulty',
              'image', 'participants', 'coach']

    def get_success_url(self):
        return reverse('project_details', kwargs={'pk': self.kwargs['pk']})
    template_name_suffix = '_update'


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project
