
from config import Config
import json
import requests

from ekamapp.utils import parse_datetime

headers = {
            "content-type": "application/json",
            "Authorization": Config.WATI_API_KEY
        }

def send_verification_message(whatsapp,name):
    try:
        print(Config.WATI_SERVER)
        url = "https://live-mt-server.wati.io/329929/api/v1/sendTemplateMessage?whatsappNumber="+whatsapp

        #payload = "{\"parameters\":[{\"name\":\"name\",\"value\":\"jaya\"}],\"template_name\":\"verification_whatsapp\",\"broadcast_name\":\"verification_whatsapp\"}"
        headers = {
            "content-type": "application/json-patch+json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3OWM4Y2RmZS03ZGQyLTRlMzAtYTk3Yy1jNWNiMGI3OTI5ZjEiLCJ1bmlxdWVfbmFtZSI6ImpheWFrdmxyQGdtYWlsLmNvbSIsIm5hbWVpZCI6ImpheWFrdmxyQGdtYWlsLmNvbSIsImVtYWlsIjoiamF5YWt2bHJAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDcvMjYvMjAyNCAwNzo0NzozNSIsImRiX25hbWUiOiJtdC1wcm9kLVRlbmFudHMiLCJ0ZW5hbnRfaWQiOiIzMjk5MjkiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBRE1JTklTVFJBVE9SIiwiZXhwIjoyNTM0MDIzMDA4MDAsImlzcyI6IkNsYXJlX0FJIiwiYXVkIjoiQ2xhcmVfQUkifQ._26_wfXxlff9KFQzNZt9kiBDcYFE-rt-OIaxTcGmMY8"
        }
            # Construct the payload with dynamic name
        payload = {
                "parameters": [
                    {
                        "name": "name",
                        "value": name
                    }
                ],
                "template_name": "verification_whatsapp",
                "broadcast_name": "verification_whatsapp"
            }
            
            # Convert the payload to a JSON string
        payload_json = json.dumps(payload)
        response = requests.post(url, data=payload_json, headers=headers)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        raise e
        


def send_ticket(name,number,event):

    print(event.event_datetime)
    date,time=parse_datetime(event.event_datetime)
    print(date,time)
    url = "https://live-mt-server.wati.io/329929/api/v1/sendTemplateMessage?whatsappNumber="+number
    #payload = "{\"parameters\":[{\"name\":\"name\",\"value\":\"jaya\"}],\"template_name\":\"verification_whatsapp\",\"broadcast_name\":\"verification_whatsapp\"}"
    headers = {
        "content-type": "application/json-patch+json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3OWM4Y2RmZS03ZGQyLTRlMzAtYTk3Yy1jNWNiMGI3OTI5ZjEiLCJ1bmlxdWVfbmFtZSI6ImpheWFrdmxyQGdtYWlsLmNvbSIsIm5hbWVpZCI6ImpheWFrdmxyQGdtYWlsLmNvbSIsImVtYWlsIjoiamF5YWt2bHJAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDcvMjYvMjAyNCAwNzo0NzozNSIsImRiX25hbWUiOiJtdC1wcm9kLVRlbmFudHMiLCJ0ZW5hbnRfaWQiOiIzMjk5MjkiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBRE1JTklTVFJBVE9SIiwiZXhwIjoyNTM0MDIzMDA4MDAsImlzcyI6IkNsYXJlX0FJIiwiYXVkIjoiQ2xhcmVfQUkifQ._26_wfXxlff9KFQzNZt9kiBDcYFE-rt-OIaxTcGmMY8"
    }
        # Construct the payload with dynamic name
    payload = {
            "parameters": [
                {
                    "name": "qrcode",
                    "value":"https://drive.google.com/uc?export=view&id=131Mfd6rBrMMNv-kqYlokfayJtPiEx09O"
                },
                {
                    "name": "name",
                    "value": name
                }
                ,
                {
                    "name": "date",
                    "value": date
                }
                ,
                {
                    "name": "time",
                    "value": time
                }
            ],
            "template_name": "ticket_message",
            "broadcast_name": "ticket_message"
        }
        
        # Convert the payload to a JSON string
    payload_json = json.dumps(payload)
    response = requests.post(url, data=payload_json, headers=headers)
    #response_json=json.dumps(response.text)
    #print(response_json["result"])
    print(response.text)
    return response.text

def send_brochure():
        pass

def send_intro_video():
        pass
    

    