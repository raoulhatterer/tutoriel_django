from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Question, Choice


# Première vue

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# C'est la vue la plus basique possible dans Django.
# Pour y accéder dans un navigateur, nous devons le mapper à une URL
# Pour cela, nous devons définir une configuration d'URL, ou « URLconf » en abrégé.
# Ces configurations d'URL sont définies dans chaque application Django, et ce sont des fichiers Python nommés urls.py.

# Autres vues:

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

def latest_questions(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# codage avec gabarit
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# codage propre avec gabarit
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)

def vote(request, question_id):
    print(59, request, question_id)
    question = get_object_or_404(Question, pk=question_id)
    # selected_choice = question.choice_set.get(pk=request.POST["choice"]) #
    try:
        print("try raoul")
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        print("selected_choice:", selected_choice)
        print("try ended raoul")
    except (KeyError, Choice.DoesNotExist):
        print("except raoul")
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

# codage avec vues génériques fondées sur des classes
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
