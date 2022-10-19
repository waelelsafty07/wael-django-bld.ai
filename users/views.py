import json
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def index(request):
    if (request.method == "GET"):
        f = open('./users/users.json', 'r')
        res = f.read()
        object_json = json.loads(res)
        return JsonResponse(object_json, safe=False)
    if (request.method == "POST"):
        f = open('./users/users.json', 'r+')
        res = f.read()
        res = json.loads(res)
        newUsers = json.loads(request.body)
        res.append(newUsers)
        strRes = str(res).replace('\'', '"')
        f.seek(0)
        f.write(strRes)
        f.truncate()
        f.close()
        return JsonResponse("New user added", safe=False)


def update_delete(request, id):
    if (request.method == "PUT"):
        f = open('./users/users.json', 'r+')
        res = f.read()
        res = json.loads(res)

        for i in range(len(res)):
            if int(res[i]["id"]) == int(id):
                reqData = json.loads(request.body)
                reqData["id"] = id
                res[i] = reqData
                break
        strRes = str(res).replace('\'', '"')
        f.seek(0)
        f.write(strRes)
        f.truncate()
        f.close()
        return JsonResponse("Updated user", safe=False)
    if (request.method == "DELETE"):
        f = open('./users/users.json', 'r+')
        res = f.read()
        res = json.loads(res)

        for i in range(len(res)):
            if int(res[i]["id"]) == int(id):
                del res[i]
                break
        strRes = str(res).replace('\'', '"')
        f.seek(0)
        f.write(strRes)
        f.truncate()
        f.close()
        return JsonResponse("Updated user", safe=False)
