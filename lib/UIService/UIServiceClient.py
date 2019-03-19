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
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class UIService(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def get_alert(self, param, context=None):
        """
        :param param: instance of type "GetAlertParam" (get_alert) ->
           structure: parameter "id" of type "AlertID"
        :returns: multiple set - (1) parameter "alert" of type "Alert" ->
           structure: parameter "id" of type "AlertID", parameter "start_at"
           of type "Timestamp" (BASE Types), parameter "end_at" of type
           "Timestamp" (BASE Types), parameter "type" of type "AlertType",
           parameter "title" of String, parameter "message" of String,
           parameter "status" of type "AlertStatus", parameter "created_at"
           of type "Timestamp" (BASE Types), parameter "created_by" of
           String, parameter "updated_at" of type "Timestamp" (BASE Types),
           parameter "updated_by" of String, (2) parameter "error" of type
           "Error" -> structure: parameter "message" of String, parameter
           "type" of String, parameter "code" of String, parameter "info" of
           unspecified object
        """
        return self._client.call_method('UIService.get_alert',
                                        [param], self._service_ver, context)

    def get_active_alerts(self, context=None):
        """
        get_active_alerts
        :returns: multiple set - (1) parameter "alerts" of list of type
           "Alert" -> structure: parameter "id" of type "AlertID", parameter
           "start_at" of type "Timestamp" (BASE Types), parameter "end_at" of
           type "Timestamp" (BASE Types), parameter "type" of type
           "AlertType", parameter "title" of String, parameter "message" of
           String, parameter "status" of type "AlertStatus", parameter
           "created_at" of type "Timestamp" (BASE Types), parameter
           "created_by" of String, parameter "updated_at" of type "Timestamp"
           (BASE Types), parameter "updated_by" of String, (2) parameter
           "error" of type "Error" -> structure: parameter "message" of
           String, parameter "type" of String, parameter "code" of String,
           parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.get_active_alerts',
                                        [], self._service_ver, context)

    def search_alerts(self, query, context=None):
        """
        :param query: instance of type "AlertQuery" (typedef structure {
           string path; string op; string value; } SearchField; typedef
           structure { string op; list<SearchField> args; }
           SearchSubExpression; typedef structure { SearchField field;
           SearchSubExpression expression; } SearchArg; typedef structure {
           string op; list<SearchArg> args; } SearchExpression;) ->
           structure: parameter "query" of type "SearchExpression" (I give up
           ...) -> unspecified object, parameter "paging" of type
           "PagingSpec" (search_alerts) -> structure: parameter "start" of
           Long, parameter "limit" of Long, parameter "sorting" of list of
           type "SortSpec" -> structure: parameter "field" of String,
           parameter "is_descending" of type "Boolean"
        :returns: multiple set - (1) parameter "result" of type
           "SearchAlertsResult" -> structure: parameter "alerts" of list of
           type "Alert" -> structure: parameter "id" of type "AlertID",
           parameter "start_at" of type "Timestamp" (BASE Types), parameter
           "end_at" of type "Timestamp" (BASE Types), parameter "type" of
           type "AlertType", parameter "title" of String, parameter "message"
           of String, parameter "status" of type "AlertStatus", parameter
           "created_at" of type "Timestamp" (BASE Types), parameter
           "created_by" of String, parameter "updated_at" of type "Timestamp"
           (BASE Types), parameter "updated_by" of String, (2) parameter
           "error" of type "Error" -> structure: parameter "message" of
           String, parameter "type" of String, parameter "code" of String,
           parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.search_alerts',
                                        [query], self._service_ver, context)

    def search_alerts_summary(self, query, context=None):
        """
        :param query: instance of type "SearchExpression" (I give up ...) ->
           unspecified object
        :returns: multiple set - (1) parameter "result" of type
           "SearchAlertsSummaryResult" -> structure: parameter "statuses" of
           mapping from String to Long, (2) parameter "error" of type "Error"
           -> structure: parameter "message" of String, parameter "type" of
           String, parameter "code" of String, parameter "info" of
           unspecified object
        """
        return self._client.call_method('UIService.search_alerts_summary',
                                        [query], self._service_ver, context)

    def am_admin_user(self, context=None):
        """
        am_admin_user
        :returns: multiple set - (1) parameter "is_admin" of type "Boolean",
           (2) parameter "error" of type "Error" -> structure: parameter
           "message" of String, parameter "type" of String, parameter "code"
           of String, parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.am_admin_user',
                                        [], self._service_ver, context)

    def add_alert(self, alert_param, context=None):
        """
        :param alert_param: instance of type "AddAlertParam" (add_alert) ->
           structure: parameter "alert" of type "Alert" -> structure:
           parameter "id" of type "AlertID", parameter "start_at" of type
           "Timestamp" (BASE Types), parameter "end_at" of type "Timestamp"
           (BASE Types), parameter "type" of type "AlertType", parameter
           "title" of String, parameter "message" of String, parameter
           "status" of type "AlertStatus", parameter "created_at" of type
           "Timestamp" (BASE Types), parameter "created_by" of String,
           parameter "updated_at" of type "Timestamp" (BASE Types), parameter
           "updated_by" of String
        :returns: multiple set - (1) parameter "result" of type
           "AddAlertResult" -> structure: parameter "id" of type "AlertID",
           (2) parameter "error" of type "Error" -> structure: parameter
           "message" of String, parameter "type" of String, parameter "code"
           of String, parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.add_alert',
                                        [alert_param], self._service_ver, context)

    def delete_alert(self, id, context=None):
        """
        :param id: instance of type "AlertID"
        :returns: multiple set - (1) parameter "result" of type
           "DeleteAlertResult" -> structure: parameter "id" of type
           "AlertID", (2) parameter "error" of type "Error" -> structure:
           parameter "message" of String, parameter "type" of String,
           parameter "code" of String, parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.delete_alert',
                                        [id], self._service_ver, context)

    def is_admin_user(self, param, context=None):
        """
        :param param: instance of type "IsAdminUserParam" -> structure:
           parameter "username" of type "Username"
        :returns: multiple set - (1) parameter "is_admin" of type "Boolean",
           (2) parameter "error" of type "Error" -> structure: parameter
           "message" of String, parameter "type" of String, parameter "code"
           of String, parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.is_admin_user',
                                        [param], self._service_ver, context)

    def update_alert(self, alert_param, context=None):
        """
        :param alert_param: instance of type "UpdateAlertParams" (update
           alert) -> structure: parameter "alert" of type "Alert" ->
           structure: parameter "id" of type "AlertID", parameter "start_at"
           of type "Timestamp" (BASE Types), parameter "end_at" of type
           "Timestamp" (BASE Types), parameter "type" of type "AlertType",
           parameter "title" of String, parameter "message" of String,
           parameter "status" of type "AlertStatus", parameter "created_at"
           of type "Timestamp" (BASE Types), parameter "created_by" of
           String, parameter "updated_at" of type "Timestamp" (BASE Types),
           parameter "updated_by" of String
        :returns: multiple set - (1) parameter "success" of type "Boolean",
           (2) parameter "error" of type "Error" -> structure: parameter
           "message" of String, parameter "type" of String, parameter "code"
           of String, parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.update_alert',
                                        [alert_param], self._service_ver, context)

    def set_alert(self, alert_param, context=None):
        """
        :param alert_param: instance of type "UpdateAlertParams" (update
           alert) -> structure: parameter "alert" of type "Alert" ->
           structure: parameter "id" of type "AlertID", parameter "start_at"
           of type "Timestamp" (BASE Types), parameter "end_at" of type
           "Timestamp" (BASE Types), parameter "type" of type "AlertType",
           parameter "title" of String, parameter "message" of String,
           parameter "status" of type "AlertStatus", parameter "created_at"
           of type "Timestamp" (BASE Types), parameter "created_by" of
           String, parameter "updated_at" of type "Timestamp" (BASE Types),
           parameter "updated_by" of String
        :returns: multiple set - (1) parameter "success" of type "Boolean",
           (2) parameter "error" of type "Error" -> structure: parameter
           "message" of String, parameter "type" of String, parameter "code"
           of String, parameter "info" of unspecified object
        """
        return self._client.call_method('UIService.set_alert',
                                        [alert_param], self._service_ver, context)

    def check_html_url(self, param, context=None):
        """
        :param param: instance of type "CheckHTMLURLParams" (Check html url)
           -> structure: parameter "url" of String
        :returns: multiple set - (1) parameter "result" of type
           "CheckHTMLURLResult" -> structure: parameter "is_valid" of type
           "Boolean", parameter "error" of type "CheckError" (Validations) ->
           structure: parameter "code" of String, parameter "info" of
           unspecified object, (2) parameter "error" of type "Error" ->
           structure: parameter "message" of String, parameter "type" of
           String, parameter "code" of String, parameter "info" of
           unspecified object
        """
        return self._client.call_method('UIService.check_html_url',
                                        [param], self._service_ver, context)

    def check_image_url(self, param, context=None):
        """
        :param param: instance of type "CheckImageURLParams" (Check image
           url) -> structure: parameter "url" of String
        :returns: multiple set - (1) parameter "result" of type
           "CheckImageURLResult" -> structure: parameter "is_valid" of type
           "Boolean", parameter "error" of type "CheckError" (Validations) ->
           structure: parameter "code" of String, parameter "info" of
           unspecified object, (2) parameter "error" of type "Error" ->
           structure: parameter "message" of String, parameter "type" of
           String, parameter "code" of String, parameter "info" of
           unspecified object
        """
        return self._client.call_method('UIService.check_image_url',
                                        [param], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('UIService.status',
                                        [], self._service_ver, context)
