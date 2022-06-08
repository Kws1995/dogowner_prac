import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data     = json.loads(request.body)

        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )

        return JsonResponse({'messasge':'created_owners'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results  = []

        for owner in owners:
           results.append(
               {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age,
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class DogsView(View):
    def post(self, request):
        data     = json.loads(request.body)

        dog = Dog.objects.create(
            owner = Owner.objects.get(id=data['owner']),
            name = data['name'],
            age = data['age'],
        )

        return JsonResponse({'messasge':'create_dogs'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results  = []

        for dog in dogs:
           results.append(
               {
                   "name" : dog.name,
                   "age" : dog.age,
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class DoglistView(View):

    def get(self, request):
        owners = Owner.objects.all()
        results  = []

        for owner in owners:
            dogs = Dog.objects.all()
            dogs_list = []
            for dog in dogs:
                if dog.owner_id == owner.id:
                    dogs_list.append(
                        {
                            "dogs_name" : dog.name,
                            "dogs_age" : dog.age
                        }
                    )
            results.append(
               {
                   "1.name" : owner.name,
                   "2.email" : owner.email,
                   "3.age" : owner.age,
                   "4.dogs_list" : dogs_list
               }
            )
       
        return JsonResponse({'resutls':results}, status=200)