from django.shortcuts import render

# Create your views here.

import json
from django.db.models.fields import EmailField

from django.shortcuts   import render
from django.http        import JsonResponse
from django.views       import View

from pets.models        import Owner, Cat

class OwnersView(View):
    def post(self, request):
        data    = json.loads(request.body)
        owner   = Owner.objects.create(
            name    = data[ 'owner_name' ],
            email   = data[ 'email' ],
            age     = data[ 'owner_age' ]
        )
        return JsonResponse({ 'MESSAGE':'Owner Info Created!' }, status = 201)

class CatsView(View):
    def post(self, request):
        data    = json.loads(request.body)
        owner   = Owner.objects.get(name = data[ 'owner_name' ])
        cat     = Cat.objects.create(
            owner   = owner,
            name    = data['cat_name'],
            age     = data['cat_age'],
        )
        return JsonResponse({ 'MESSAGE':'Cat Info Created!' }, status = 201)