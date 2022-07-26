from tetpyclient import RestClient
import json


#
# credentials.json
#
# {
#     "api_key": "abcd1234",
#     "api_secret": "1234abcd"
# }
#


#
# api_endpoint.json
# {
#     "API_ENDPOINT": "https://my_tetration dashboard.com"
# }
#

# Open the JSON file and get the API Endpoint URL
with open('api_endpoint.json', 'r') as openfile:
    json_object = json.load(openfile)

API_ENDPOINT = json_object['API_ENDPOINT']


def get_tet_data(api_request):

    restclient = RestClient(API_ENDPOINT,
                            credentials_file='./credentials.json',
                            verify=True)
    # followed by API calls, for example API to retrieve list of agents.
    # API can be passed /openapi/v1/sensors or just /sensors.

    resp = restclient.get(api_request)

    # Check to see if it worked
    if resp.reason == 'OK':
        json_resp = resp.json()

        if type(json_resp) is list:
            print("Detected a list", json_resp)
            print()

            for x in json_resp:
                print(x)

        elif type(json_resp) is dict:
            print("Detected a dict", json_resp)
            print()

            for k, v in json_resp.items():
                print(k, v)
                print()
                for x in v:
                    print(x)
    else:
        print("Access Denied !", resp)


if __name__ == '__main__':
    # api_request = '/sensors/62f58c51a030e90f1e8ff6db137a50b0f197be81'
    # api_request = '/cluster_nodes'
    # api_request = '/applications'
    # api_request = '/users'
    api_request = '/sensors'

    get_tet_data(api_request)



