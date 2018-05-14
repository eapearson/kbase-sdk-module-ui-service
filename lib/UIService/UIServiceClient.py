# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class UIService(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def get_alert(self, id, context=None):
        """
        get_alert
        :param id: instance of type "AlertID"
        :returns: instance of type "Alert" -> structure: parameter "id" of
           type "AlertID", parameter "start_at" of type "Timestamp" (BASE
           Types), parameter "end_at" of type "Timestamp" (BASE Types),
           parameter "type" of type "AlertType", parameter "title" of String,
           parameter "message" of list of String, parameter "status" of type
           "AlertStatus"
        """
        return self._client.call_method(
            'UIService.get_alert',
            [id], self._service_ver, context)

    def get_active_alerts(self, context=None):
        """
        get_active_alerts
        :returns: instance of list of type "Alert" -> structure: parameter
           "id" of type "AlertID", parameter "start_at" of type "Timestamp"
           (BASE Types), parameter "end_at" of type "Timestamp" (BASE Types),
           parameter "type" of type "AlertType", parameter "title" of String,
           parameter "message" of list of String, parameter "status" of type
           "AlertStatus"
        """
        return self._client.call_method(
            'UIService.get_active_alerts',
            [], self._service_ver, context)

    def search_alerts(self, query, context=None):
        """
        :param query: instance of type "Query" (search_alerts) -> unspecified
           object
        :returns: instance of list of type "Alert" -> structure: parameter
           "id" of type "AlertID", parameter "start_at" of type "Timestamp"
           (BASE Types), parameter "end_at" of type "Timestamp" (BASE Types),
           parameter "type" of type "AlertType", parameter "title" of String,
           parameter "message" of list of String, parameter "status" of type
           "AlertStatus"
        """
        return self._client.call_method(
            'UIService.search_alerts',
            [query], self._service_ver, context)

    def am_admin_user(self, context=None):
        """
        am_admin_user
        :returns: instance of type "Boolean"
        """
        return self._client.call_method(
            'UIService.am_admin_user',
            [], self._service_ver, context)

    def add_alert(self, alert, context=None):
        """
        ADMIN
        :param alert: instance of type "AddAlertParams" (add_alert) ->
           structure: parameter "alert" of type "Alert" -> structure:
           parameter "id" of type "AlertID", parameter "start_at" of type
           "Timestamp" (BASE Types), parameter "end_at" of type "Timestamp"
           (BASE Types), parameter "type" of type "AlertType", parameter
           "title" of String, parameter "message" of list of String,
           parameter "status" of type "AlertStatus"
        :returns: instance of type "AlertID"
        """
        return self._client.call_method(
            'UIService.add_alert',
            [alert], self._service_ver, context)

    def delete_alert(self, id, context=None):
        """
        :param id: instance of type "AlertID"
        """
        return self._client.call_method(
            'UIService.delete_alert',
            [id], self._service_ver, context)

    def is_admin_user(self, username, context=None):
        """
        :param username: instance of type "Username"
        :returns: instance of type "Boolean"
        """
        return self._client.call_method(
            'UIService.is_admin_user',
            [username], self._service_ver, context)

    def update_alert(self, alert, context=None):
        """
        :param alert: instance of type "AddAlertParams" (add_alert) ->
           structure: parameter "alert" of type "Alert" -> structure:
           parameter "id" of type "AlertID", parameter "start_at" of type
           "Timestamp" (BASE Types), parameter "end_at" of type "Timestamp"
           (BASE Types), parameter "type" of type "AlertType", parameter
           "title" of String, parameter "message" of list of String,
           parameter "status" of type "AlertStatus"
        """
        return self._client.call_method(
            'UIService.update_alert',
            [alert], self._service_ver, context)

    def set_alert_status(self, id, status, context=None):
        """
        set_alert_status
        :param id: instance of type "AlertID"
        :param status: instance of type "AlertStatus"
        """
        return self._client.call_method(
            'UIService.set_alert_status',
            [id, status], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('UIService.status',
                                        [], self._service_ver, context)
