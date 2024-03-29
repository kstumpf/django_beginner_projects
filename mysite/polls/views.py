# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from polls.models import Poll, Choice

# Raising a 404 error.
# from django.http import Http404

# from django.contrib.auth.decorators import login_required
# We will use this instead of our index function.
# @login_required(login_url='/accounts/login/')
class IndexView(generic.ListView):
    # Limiting access to logged-in users that pass a test.
    # if not '@example.com' in request.user.email:
    #    return HttpResponse("You can't vote in this poll.")
    # else: template_name = ...
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five pulished polls."""
        return Poll.objects.filter(
        pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def index(request):
    # return HttpResponse("Hello, world. You're at the poll index.")
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list,
    # })
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context))

def detail(request, poll_id):
    # return HttpResponse("You're looking at poll %s." % poll_id)
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    # return HttpResponse("You're looking at the results of poll %s." % poll_id)
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})


# THIS MUST REMAIN in addition to our new Generic View classes.
def vote(request, poll_id):
    # return HttpResponse("You're voting on poll%s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
