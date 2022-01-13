# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Feeds.models import Feeds
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    NotFound,
)
from .serializers import (
    FeedsSerializer,
)
from rest_framework.permissions import IsAuthenticated



class FeedsListApiView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        feeds = Feeds.objects.all()
        serializer = FeedsSerializer(feeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


STATUS_CODE = "code"
MESSAGE = "msg"
DATA = 'data'

INVALID_POST_DATA = "7700"
USER_EMAIL_ALREADY_EXIST = "9003"
USER_CREATE_SUCCESS = "2999"
BAD_REQUEST = "0000"
INVALID_LOGIN = "2304"
UNAUTHORIZED_LOGIN = "2305"
LOGIN_SUCCESS = "2300"
INVALID_USER = "9000"




RESPONSE_LOOKUP = {
BAD_REQUEST: {
    STATUS_CODE: int(BAD_REQUEST),
    MESSAGE: "Bad request provided"
},
INVALID_POST_DATA: {
    STATUS_CODE: int(INVALID_POST_DATA),
    MESSAGE: "Invalid or no data provided."
},

USER_EMAIL_ALREADY_EXIST: {
    STATUS_CODE: int(USER_EMAIL_ALREADY_EXIST),
    MESSAGE: "User with given email already exists"
},
USER_CREATE_SUCCESS: {
    STATUS_CODE: int(USER_CREATE_SUCCESS),
    MESSAGE: "User created successfully"
},
    INVALID_LOGIN: {
        STATUS_CODE: int(INVALID_LOGIN),
        MESSAGE: "Invalid email provided."
    },
    UNAUTHORIZED_LOGIN: {
        STATUS_CODE: int(UNAUTHORIZED_LOGIN),
        MESSAGE: "Not a member. Please signup"
    },
    LOGIN_SUCCESS: {
        STATUS_CODE: int(LOGIN_SUCCESS),
        MESSAGE: "Successfully logged in."
    },
    INVALID_USER: {
        STATUS_CODE: int(INVALID_USER),
        MESSAGE: "Invalid user. Authentication token may be wrong."
    },
}

def get_response_dict(lookup, data=None, substitute=None):
    response_data = copy(RESPONSE_LOOKUP.get(lookup, {
        STATUS_CODE: 0,
        MESSAGE: "Something Went Wrong",
        DATA: ''
    }))
    if data is not None:
        response_data[DATA] = data
    if substitute:
        response_data[MESSAGE] = response_data[MESSAGE] % substitute
    return response_data

