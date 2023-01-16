import requests

def new_post(ap_instance, api_key, post):
    api_path = "/api/v1/statuses?federated=true"
    api_url = ap_instance + api_path
    full_post_req = post + "&sensitive=false"
    api_post_values = {'Authorization: Bearer':api_key, "accept":"application/json","Content-Type":"application/json","Status":full_post_req}
    requests.post(api_url, data=api_post_values)
