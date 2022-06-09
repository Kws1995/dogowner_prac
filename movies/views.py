import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie

class ActorsView(View):
    def post(self, request):
        data     = json.loads(request.body)
        print(data)
        actors = Actor.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['date_of_birth'],
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        actors_list  = []

        for actor in actors:
            movies = actor.movies.all()
            movies_list  = []
            for movie in movies:
                    movies_list.append({"title":movie.title})
            actors_list.append(
                {
                            "1.first_name" : actor.first_name,
                            "2.last_name" : actor.last_name,
                            "3.date_of_birth" : actor.date_of_birth,
                            'title_list': movies_list
                }
            )
        return JsonResponse({'resutls':actors_list}, status=200)

class MoviesView(View):
    def post(self, request):
        data     = json.loads(request.body)
        movies = Movie.objects.create(
            title = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time'],
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        movies_list  = []

        for movie in movies:
            actors = movie.actor_set.all()
            actors_list  = []
            for actor in actors:
                actors_list.append({"actor":(actor.first_name)+(actor.last_name)})
            movies_list.append(
                {
                    "1.title" : movie.title,
                    "2.release_date" : movie.release_date,
                    "3.running_time" : movie.running_time,
                    "actors_list" : actors_list
                }
            )
        return JsonResponse({'resutls':movies_list}, status=200)