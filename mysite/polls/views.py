from django.http import HttpResponse
#from django.template import Context, loader
from polls.models import Poll
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})

# def detail(request, poll_id):
#     try:
#         p = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#     return render_to_response('polls/detail.html', {'poll': p})

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     t = loader.get_template('polls/index.html')
#     c = Context({
#         'latest_poll_list': latest_poll_list,
#     })
#     return HttpResponse(t.render(c))

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     output = ', '.join([p.question for p in latest_poll_list])
#     return HttpResponse(output)

#def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

# def detail(request, poll_id):
#     return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
