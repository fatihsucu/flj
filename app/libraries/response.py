# -*- coding: utf8 -*-
"""
"""
import json

# @TODO: liste doldurulacak
_RESPONSES = {
    19: "Unexpected error. We are warned.",
    20: "Success.",
    21: "Email or password is incorrect.",
    22: "Email is already taken.",
    23: "Email and password are required.",
    24: "Email address can not be empty.",
    25: "Email is invalid.",
    26: "Credential_id is not valid",
    27: "Password must be at least 6 letters.",
    28: "The verification code is invalid.",
    29: "You reached the number of limit.",
    30: "An error occured. We'll check this.",
    31: "You need to log in to carry out this operation.",
    32: "Agent not found.",
    33: "Activation Id is required.",
    34: "Password required for this operation.",
    35: "Email required for this operation.",
    36: "Not authorized.",
    37: "Agent ID is required.",
    38: "Field '%s' required.",
    39: "Credential or email are invalid.",
    40: "Couldn't find any conversation for visitor.",
    41: "We have a problem in db connection.",
    42: "Couldn't remove history.",
    43: "Already activated.",
    44: "Visitor id required for this operation",
    45: "displayName can not be empty",
    46: "status can not be empty",
    47: "Visitor already registered",
    48: "visitorId is not an ObjectId",
    49: "Couldn't find visitor for update",
    50: "Couldn't find visitor",
    51: "Your account is disabled.",
    52: "One or more arguments are not valid.",
    53: "You can not delete yourself.",
    54: "You can not update your status.",
    55: "Name can not be empty.",
    56: "Shortcut keyword already exists.",
    57: "Shortcut not found.",
    58: "keyword and message can not empty.",
    59: "Couldn't find any messages in this conversation",
    60: "Couldn't find any rooms",
    61: "Not allowed",
    62: "question, answer and category can not empty.",
    63: "question already exists.",
    64: "question not found.",
    65: "special question can not delete.",
    66: "A robot account cannot be deleted",
    67: "You can't change your role.",
    68: "Manager not found.",
    68: "Account id not found.",
    69: "referer not found.",
    70: "Activation needed.",
    71: "Couldn't find any account",
    300: "any widget status not found.",  # widget errors between 300 and 350
    301: "widget pinging encountered an error.",
    302: "getting widget stats encountered an error.",
    400: "settings not found.",  # settings messages between 400 and 500
    401: "settings cannot be saved due to some wrong arguments.",
}


class JSONEncoder(json.JSONEncoder):
    """
    This is a monkey patch to extend the serialization ability of the json
    library. Most of time your data includes arbitrary objects which are not
    json serializable. This patch try to serialize data with the default
    methods. If it failds, then, it tries to serilalize them as string.
    """
    def default(self, o):
        try:
            return json.JSONEncoder.default(self, o)
        except Exception, e:
            return str(o)
        raise TypeError("{} is not seriaalizable".format(o.__class__.__name__))


def make(responseCode, data=None):
    return makeRaw(responseCode, _RESPONSES[responseCode], data)


def makeRaw(statusCode, statusMessage, data=None):
    response = {}
    response['status'] = {
        'code': statusCode,
        'message': statusMessage}

    if data:
        response['data'] = data

    return JSONEncoder().encode(response)
