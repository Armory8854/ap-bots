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
        r = requests.post(api_url, headers=api_post_headers, json=api_post_values)
        print(r)
        if r == str("<Response [200]>"):
            print('Post successful!')
        else:
            print('Post NOT Successful!')
    elif was_i_posted == 1:
        print("Post already made. Moving on...")
        exit
    else:
        print("Something went wrong...")
        print("was_i_posted returns: " + str(was_i_posted))
        exit
