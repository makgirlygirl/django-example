from django.urls import path, include
from .views import helloAPI, randomQuiz

# hello 앱에 있는 url을 관리한다.
urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]