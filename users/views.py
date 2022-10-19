import json
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def index(request):

    # @url /api/
    # @prams /
    # @desc GET method Fetch  all users
    if (request.method == "GET"):
        f = open('./users/users.json', 'r')
        res = f.read()
        object_json = json.loads(res)
        return JsonResponse(object_json, safe=False)
    # @url /api/
    # @prams /
    # @desc POST method Create ne user
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
    # @url /api/<int:id>
    # @prams id
    # @desc PUT method update user
    if (request.method == "PUT"):
        f = open('./users/users.json', 'r+')
        res = f.read()
        res = json.loads(res)
        x = -1
        for i in range(len(res)):
            if int(res[i]["id"]) == int(id):
                x = i
                break
        if (x == -1):
            return JsonResponse("Not found user", safe=False)
        else:
            reqData = json.loads(request.body)
            reqData["id"] = id
            res[i] = reqData
            strRes = str(res).replace('\'', '"')
            f.seek(0)
            f.write(strRes)
            f.truncate()
            f.close()
            return JsonResponse("Updated user", safe=False)
    # @url /api/<int:id>
    # @prams id
    # @desc PUT method delete user
    if (request.method == "DELETE"):
        f = open('./users/users.json', 'r+')
        res = f.read()
        res = json.loads(res)
        x = -1
        for i in range(len(res)):
            if int(res[i]["id"]) == int(id):
                x = i
                break
        if (x == -1):
            return JsonResponse("Not found user", safe=False)
        else:
            del res[i]
            strRes = str(res).replace('\'', '"')
            f.seek(0)
            f.write(strRes)
            f.truncate()
            f.close()
            return JsonResponse("Delete user", safe=False)
