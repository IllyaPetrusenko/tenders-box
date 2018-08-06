import requests, json
from monitoring.test_data import *
from monitoring.files_mon import *


# def send_file_to_doc_service():
#
#     req = requests.post(doc_service_url, headers=headers1, files=files)
#     req = req.text
#     return req
#
#
# documents = [send_file_to_doc_service()]


class Monitoring:

    @staticmethod
    def draft_monitoring():

        monitoring = requests.post(url, data=json.dumps(payload), headers=headers)

        return monitoring.text

    # New monitoring + activation
    @staticmethod
    def active_monitoring():

        monitoring_id = Monitoring.draft_monitoring()
        requests.patch("{}/{}".format(url, monitoring_id), data=decision(), headers=headers)
        resp = requests.patch("{}/{}".format(url, monitoring_id), data=monitoring_status('active'), headers=headers)
        monitoring_id = resp.json()['data']['id']

        return monitoring_id

    # New monitoring + 5 posts
    @staticmethod
    def post_monitoring():

        monitoring_id = Monitoring.active_monitoring()
        for i in range(5):
            requests.post(url + '/' + monitoring_id + '/posts', data=json.dumps(msg), headers=headers)
        return monitoring_id

    # New monitoring ---> activate ----> addressed
    @staticmethod
    def make_conclusion_and_adress():

        monitoring_id = Monitoring.post_monitoring()
        requests.patch(url + '/' + monitoring_id, data=json.dumps(conclusion(documents, True)), headers=headers)
        requests.patch(url + '/' + monitoring_id, data=json.dumps(adressed), headers=headers)
        return monitoring_id

    # New monitoring ---> activate ----> addressed ---> stopped
    @staticmethod
    def stop_monitoring():
        monitoring_id = make_conclusion_and_adress()
        resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(stopped), headers=headers)
        return monitoring_id

    # New monitoring ---> activate ----> addressed ---> complete
    @staticmethod
    def complete_monitoring():
        monitoring_id = make_conclusion_and_adress()
        resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(complete), headers=headers)
        return resp.json()

    # New monitoring ---> activate ----> declined ---> closed
    @staticmethod
    def close_monitoring():
        monitoring_id = '89fdc6a2aa714cfbb26ae70c1d5a9507'
        requests.patch(url + '/' + monitoring_id, data=json.dumps(conclusion(documents, False)), headers=headers)
        # requests.patch(url + monitoring_id,
        #                data=json.dumps(eliminationResolution), headers=headers)
        resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(decline), headers=headers)
        return resp.text
