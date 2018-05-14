# -*- coding: utf-8 -*-
#BEGIN_HEADER
from UIService.UIServiceModel import UIServiceModel
#END_HEADER


class UIService:
    '''
    Module Name:
    UIService

    Module Description:
    A KBase module: UIService
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "HEAD"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.data_root = config['data-root']
        self.model_path = self.data_root + '/model.db'
        print('auth config: %s, %s' % (config['auth-url'], config['auth-service-url']))
        model = UIServiceModel(path=self.model_path, auth_url=config['auth-url'])
        model.initialize()

        # self.authUrl = config['auth-service-url']
        # self.authUrl = 'https://ci.kbase.us/services/auth'
        self.auth_url = config['auth-url']

        #END_CONSTRUCTOR
        pass


    def get_alert(self, ctx, id):
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
        # ctx is the context object
        # return variables are: alert
        #BEGIN get_alert
        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url, token=ctx['token'])
        alert = model.get_alert(id) 
        #END get_alert

        # At some point might do deeper type checking...
        if not isinstance(alert, dict):
            raise ValueError('Method get_alert return value ' +
                             'alert is not type dict as required.')
        # return the results
        return [alert]

    def get_active_alerts(self, ctx):
        """
        get_active_alerts
        :returns: instance of list of type "Alert" -> structure: parameter
           "id" of type "AlertID", parameter "start_at" of type "Timestamp"
           (BASE Types), parameter "end_at" of type "Timestamp" (BASE Types),
           parameter "type" of type "AlertType", parameter "title" of String,
           parameter "message" of list of String, parameter "status" of type
           "AlertStatus"
        """
        # ctx is the context object
        # return variables are: alerts
        #BEGIN get_active_alerts
        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url, token=ctx['token'])
        alerts = model.get_active_alerts()
        #END get_active_alerts

        # At some point might do deeper type checking...
        if not isinstance(alerts, list):
            raise ValueError('Method get_active_alerts return value ' +
                             'alerts is not type list as required.')
        # return the results
        return [alerts]

    def search_alerts(self, ctx, query):
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
        # ctx is the context object
        # return variables are: alerts
        #BEGIN search_alerts
        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url, token=ctx['token'])
        alerts = model.search_alerts()
        #END search_alerts

        # At some point might do deeper type checking...
        if not isinstance(alerts, list):
            raise ValueError('Method search_alerts return value ' +
                             'alerts is not type list as required.')
        # return the results
        return [alerts]

    def am_admin_user(self, ctx):
        """
        am_admin_user
        :returns: instance of type "Boolean"
        """
        # ctx is the context object
        # return variables are: is_admin
        #BEGIN am_admin_user
        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url,  token=ctx['token'])
        is_admin = model.authorized_user_is_admin()
        #END am_admin_user

        # At some point might do deeper type checking...
        if not isinstance(is_admin, int):
            raise ValueError('Method am_admin_user return value ' +
                             'is_admin is not type int as required.')
        # return the results
        return [is_admin]

    def add_alert(self, ctx, alert):
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
        # ctx is the context object
        # return variables are: alert_id
        #BEGIN add_alert
        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url, token=ctx['token'])
        alert_id = model.add_alert(alert)
        #END add_alert

        # At some point might do deeper type checking...
        if not isinstance(alert_id, int):
            raise ValueError('Method add_alert return value ' +
                             'alert_id is not type int as required.')
        # return the results
        return [alert_id]

    def delete_alert(self, ctx, id):
        """
        :param id: instance of type "AlertID"
        """
        # ctx is the context object
        #BEGIN delete_alert

        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url, token=ctx['token'])
        model.delete_alert(id) 
        #END delete_alert
        pass

    def is_admin_user(self, ctx, username):
        """
        :param username: instance of type "Username"
        :returns: instance of type "Boolean"
        """
        # ctx is the context object
        # return variables are: is_admin
        #BEGIN is_admin_user
        model = UIServiceModel(path=self.model_path, auth_url=self.auth_url, token=ctx['token'])
        model.ensure_admin_authorization()
        is_admin = model.is_admin_user(username)
        #END is_admin_user

        # At some point might do deeper type checking...
        if not isinstance(is_admin, int):
            raise ValueError('Method is_admin_user return value ' +
                             'is_admin is not type int as required.')
        # return the results
        return [is_admin]

    def update_alert(self, ctx, alert):
        """
        :param alert: instance of type "AddAlertParams" (add_alert) ->
           structure: parameter "alert" of type "Alert" -> structure:
           parameter "id" of type "AlertID", parameter "start_at" of type
           "Timestamp" (BASE Types), parameter "end_at" of type "Timestamp"
           (BASE Types), parameter "type" of type "AlertType", parameter
           "title" of String, parameter "message" of list of String,
           parameter "status" of type "AlertStatus"
        """
        # ctx is the context object
        #BEGIN update_alert
        #END update_alert
        pass

    def set_alert_status(self, ctx, id, status):
        """
        set_alert_status
        :param id: instance of type "AlertID"
        :param status: instance of type "AlertStatus"
        """
        # ctx is the context object
        #BEGIN set_alert_status
        #END set_alert_status
        pass
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
