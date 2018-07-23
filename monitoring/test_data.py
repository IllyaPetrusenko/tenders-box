from monitoring.key import *

headers1 = {'authorization': 'Basic {}'.format(ds_key)}

doc_service_url = 'https://upload.docs-sandbox.openprocurement.org/upload'


files = {'file': open('/home/qa1/Изображения/146796919019803402.png', 'rb')}


url = 'https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings'

headers = {
    'Authorization': "Basic OWIzYWFhZmJhOWZlNGY0Yzk1YzNiZTNlMWZlYWFlMzE6",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "0acb6f32-d856-44f4-9234-77c46981366b"
    }

tender_id = 'f274f3100d8f438ea8de5542748a757c'

payload = {
  "data": {
    "monitoringDetails": "accelerator=1440",
    "reasons": [
      "public",
      "fiscal"
    ],
    "tender_id": tender_id,
    "procuringStages": [
      "awarding",
      "contracting"
    ],
    "parties": [
      {
        "contactPoint": {
          "name": "Oleksii Kovalenko",
          "telephone": "0440000000"
        },
        "identifier": {
          "scheme": "UA-EDR",
          "id": "40165856",
          "uri": "http://www.dkrs.gov.ua"
        },
        "name": "The State Audit Service of Ukraine",
        "roles": [
          "risk_indicator"
        ],
        "address": {
          "countryName": "Ukraine",
          "postalCode": "04070",
          "region": "Kyiv",
          "streetAddress": "Petra Sahaidachnoho St, 4",
          "locality": "Kyiv"
        }
      }
    ]
  }
}


def decision(documents):
    payload2 = {
      "data": {
        "decision": {
          "date": "2018-01-02T01:05:00",
          "description": "Опис підстав для здійсненнjjjjjjjjjjjjjjjjjjjjjjjjя моніторинг",
          "documents": documents
        }
      }
    }
    return payload2

activate = {
  "data": {
    "status": "active"
  }
}

msg = {
  "data": {
    "title": "Тайтл диалога5",
    "description": "Описание диалога5"
  }
}


def conclusion(violation, documents = 0):

    if violation is True:

        conclusion_cont = {
          "data": {
            "conclusion": {
              "violationType": [
                "documentsForm",
                "corruptionAwarded"
              ],
              "description": "Ashes, ashes, we all fall down",
              "stringsAttached": "Pocket full of posies",
              "auditFinding": "Ring around the rosies",
              "violationOccurred": True,
              "documents": documents
            }
          }
        }

    elif violation is False:

        conclusion_cont = {
            "data": {
                "conclusion": {
                    "violationType": [
                        "documentsForm",
                        "corruptionAwarded"
                    ],
                    "description": "Ashes, ashes, we all fall down",
                    "stringsAttached": "Pocket full of posies",
                    "auditFinding": "Ring around the rosies",
                    "violationOccurred": False,
                    "documents": documents
                }
            }
        }
    return conclusion_cont

adressed = {
  "data": {
    "status": "addressed"
  }
}


stopped = {
  "data": {
    "status": "stopped",
    "cancellation": {
      "relatedParty": "be546d6519ee37a597df5c1ca71ddd18",
      "description": "Complaint was created"
    }
  }
}


complete = {
  "data": {
    "status": "completed"
  }
}


decline = {
  "data": {
    "status": "declined"
  }
}

eliminationResolution = {
  "data": {
    "eliminationResolution": {
      "description": "The award hasn't been fixed.",
      "relatedParty": "f0e119b94ed33bd9b72caf2573503984",
      "resultByType": {
        "corruptionAwarded": "not_eliminated",
        "documentsForm": "eliminated"
      },
      "result": "partly"
    }
  }
}

def monitoring_status(status):

    mon_status = {
  "data": {
    "status": status
  }
}
    return mon_status

print(monitoring_status('active'))