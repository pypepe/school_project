import json
# from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


subjects = [{"id": 1, "name": "Maths"}, {"id": 2, "name": "PE"}]


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

@csrf_exempt
def subject_detail(request, pk):
    global subjects

    try:
        subject = next(subject for subject in subjects if subject["id"] == pk)
    except StopIteration:
        return JsonResponse({"status": f"There is no subject with id {pk}"}, status=404)
 
    if request.method == "GET":
        return JsonResponse(subject)
