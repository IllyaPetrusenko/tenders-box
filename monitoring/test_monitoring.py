import requests, json
from monitoring.test_data import *


def send_file_to_doc_service():

    req = requests.post(doc_service_url, headers=headers1, files=files)
    req = req.json()
    return req['data']

documents = [send_file_to_doc_service()]

def draft_monitoring():

    monitoring = requests.post(url, data=json.dumps(payload), headers=headers)
    monitoring_id = monitoring.json()['data']['id']
    monitoring_good = monitoring.json()['data']['monitoring_id']
    return monitoring_id, monitoring_good


# New monitoring + activation
def active_monitoring():

    monitoring_id = '89fdc6a2aa714cfbb26ae70c1d5a9507'
    requests.patch(url + '/' + monitoring_id, data=json.dumps(decision(documents)), headers=headers)
    resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(activate), headers=headers)
    return resp.json()


# New monitoring + 5 posts
def post_monitoring():

    monitoring_id = '89fdc6a2aa714cfbb26ae70c1d5a9507'
    for i in range(5):
        requests.post(url + '/' + monitoring_id + '/posts', data=json.dumps(msg), headers=headers)
    return monitoring_id


# New monitoring ---> activate ----> addressed
def make_conclusion_and_adress():

    monitoring_id = post_monitoring()
    requests.patch(url + '/' + monitoring_id, data=json.dumps(conclusion(documents, True)), headers=headers)
    requests.patch(url + '/' + monitoring_id, data=json.dumps(adressed), headers=headers)
    return monitoring_id


# New monitoring ---> activate ----> addressed ---> stopped
def stop_monitoring():
    monitoring_id = make_conclusion_and_adress()
    resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(stopped), headers=headers)
    return monitoring_id


# New monitoring ---> activate ----> addressed ---> complete
def complete_monitoring():
    monitoring_id = make_conclusion_and_adress()
    resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(complete), headers=headers)
    return resp.json()


# New monitoring ---> activate ----> declined ---> closed
def close_monitoring():
    monitoring_id = '89fdc6a2aa714cfbb26ae70c1d5a9507'
    requests.patch(url + '/' + monitoring_id, data=json.dumps(conclusion(documents, False)), headers=headers)
    # requests.patch(url + monitoring_id,
    #                data=json.dumps(eliminationResolution), headers=headers)
    resp = requests.patch(url + '/' + monitoring_id, data=json.dumps(decline), headers=headers)
    return resp.text

print(close_monitoring())