from django.views.generic import ListView
from stage.models import StageTasks
from tasks.models import Tasks

class StageListView(ListView):
    model = StageTasks
    template_name = 'pipeline.html'
    context_object_name = 'stage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Tasks.objects.all()
        context['tasks'] = tasks
        return context