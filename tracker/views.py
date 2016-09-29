from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, render
from .models import Story, Evaluation


# Create your views here.
@login_required
def index(request):
    stories = Story.objects.all()
    evaluation = Evaluation.objects.get(user=request.user)
    for story in stories:
        print(story.evaluation_set.aggregate(Avg('estimate')))
        story.average = story.evaluation_set.aggregate(Avg('estimate'))['estimate__avg']
    return render(request, 'stories/index.html', {'stories': stories, 'user': request.user, 'evaluation': evaluation})

@login_required
def evaluate(request):
    story = get_object_or_404(Story, pk=request.POST['story'])
    evaluation = Evaluation(user=request.user, story=story, estimate=request.POST['estimate'])
    evaluation.save()
    return redirect('stories:index')
