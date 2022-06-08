from django.urls import path

from owners.views import OwnersView, DogsView, DoglistView

urlpatterns = [
    path('/owner', OwnersView.as_view()),
    path('/dog', DogsView.as_view()),
    path('/dogowner', DoglistView.as_view())
]
