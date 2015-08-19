# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import threading

import boto3

__all__ = ['get']

_LOCK = threading.Lock()
_CLIENTS = {}


class AutoScaling(object):

    def __init__(self, name):
        self._client = boto3.Session(profile_name=name).client('autoscaling')

    def get_schedule(self, **kwargs):
        response = self._client.describe_scheduled_actions(**kwargs)
        return response['ScheduledUpdateGroupActions']


def get(name):
    global _CLIENTS
    if name in _CLIENTS:
        return _CLIENTS[name]

    return _set_and_get(name)


def _set_and_get(name):
    global _LOCK
    global _CLIENTS

    with _LOCK:
        if name in _CLIENTS:
            return _CLIENTS[name]

        result = _CLIENTS[name] = AutoScaling(name)

    return result
