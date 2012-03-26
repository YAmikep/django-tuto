from django.http import HttpResponse
from django.template import Context, loader
from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))
    
# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     output = ', '.join([p.question for p in latest_poll_list])
#     return HttpResponse(output)

#def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
