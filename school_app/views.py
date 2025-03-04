import json
# from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


subjects = [{"name": "Maths"}, {"name": "PE"}]


def hello_world(request):

    return HttpResponse("Hello Informatika s Misom")


@csrf_exempt
def list_subjects(request):
    if request.method == "GET":
        return JsonResponse(subjects, safe=False, status=200)
    elif request.method == "POST":
        subject = request.body
        print(subject)
        print(type(subject))

        subject_dict = json.loads(subject)

        print(subject_dict)
        print(type(subject_dict))
        subjects.append(subject_dict)
        # return HttpResponse(subjects)
        return JsonResponse(subject_dict, status=200)
    else:
        return HttpResponseNotFound("Sorry, this method is not supported")
