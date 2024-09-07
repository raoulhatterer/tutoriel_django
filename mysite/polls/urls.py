from django.urls import path

from . import views

app_name = "polls"


print(f"Je viens d'exécuter le fichier {app_name}/urls.py")

urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # old path("", views.index, name="index"), # ou views.index appelle la fonction index(request) définie dans le fichier views.py de l'application
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # old path("<int:question_id>/", views.detail, name="detail"), # the 'name' value as called by the {% url %} template tag
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # old path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # old path("<int:question_id>/vote/", views.vote, name="vote"),
    # ex: /latest_questions/
    path("latest_questions/", views.latest_questions, name="latest"),
]





# sur l'utilité de name : https://stackoverflow.com/a/68307313/5952631
# `{% url 'NAME OF URL here' any_variables_here %}`
# NAME OF URL signifie le nom que nous donnons à une URL dans l'argument name de path(),
# ce qui signifie que nous devons uniquement utiliser le nom de l'URL dans l'attribut href,
# nous n'avons plus besoin d'utiliser l'URL complexe partout dans notre code,
# c'est une fonctionnalité géniale de Django.
