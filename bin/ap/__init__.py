import requests

def new_post(ap_instance, api_key, post, link, was_i_posted):
    api_path = "/api/v1/statuses?federated=true"
    api_url = ap_instance + api_path
    full_post_req = post + " - " + link
    api_post_values = {"Status":full_post_req}
    api_post_headers = {"Authorization": "Bearer YZVJNMU3MWYTN2Q4NS0ZOGY5LWJKYJETMWIXMTM2MMZIMWQ1",
                        "accept":"application/json",
                        "Content-Type":"application/json",}
    if was_i_posted == 0:
        requests.post(api_url, headers=api_post_headers, json=api_post_values)
        print('Post successful!')
    elif was_i_posted == 1:
        print("Post already made. Moving on...")
        exit
    else:
        print("Something went wrong...")
        print("was_i_posted returns: " + str(was_i_posted))
        exit

def new_app(ap_instance, app_name):
    api_url = ap_instance + "/api/v1/apps"
    new_app_data = {"client_name":app_name,
                    "redirect_uris":"urn:ietf:wg:oauth:2.0:oob",
                    "scopes":"read write push",
                    "website":ap_instance}
    r = requests.post(api_url, data=new_app_data)
    print(r.text[0])
    
