from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail

from .forms import ContactForm, MyForm

from .models import Question, Choice

def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  context = {"latest_question_list": latest_question_list}
  return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "latest_question_list"

  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.order_by("-pub_date")[:5]

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {"question": question}
  return render(request, "polls/detail.html", context)

class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html"


def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

class ResultsView(generic.DetailView):
  model = Question
  template_name = "polls/results.html"


def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    context = {
      "question": question,
      "error_message": "You didn't select a choice.",
    }
    return render(request, "polls/detail.html", context)
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {"question": question}
  return render(request, "polls/results.html", context)

def contact_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        print('Form - POST: ', form)
        
        if form.is_valid():
          subject = form.cleaned_data["subject"]
          message = form.cleaned_data["message"]
          sender = form.cleaned_data["sender"]
          cc_myself = form.cleaned_data["cc_myself"]

          recipients = ["pauloroberto_nobrega@hotmail.com"]
          if cc_myself:
              recipients.append(sender)

          send_mail(subject, message, sender, recipients)
          return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, "polls/form.html", {"form": form})


def name_form(request):
  form = MyForm()
  return render(request, "polls/form.html", {"form": form})