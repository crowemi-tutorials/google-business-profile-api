import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/business.manage'
]
GOOGLE_ANALYTICS_CONFIG_PATH = '.secrets/client_secrets.json'

def main():
    try:
        # The from_service_account_file method is used to create a Credentials object from a service account key file.
        credentials = service_account.Credentials.from_service_account_file(filename=GOOGLE_ANALYTICS_CONFIG_PATH)

        # The with_scopes method is used to specify the scopes a credential should have access to.
        scoped_credentials = credentials.with_scopes(SCOPES)

        # The build method is used to create a service object.
        service = build('mybusinessbusinessinformation', 'v1', credentials=scoped_credentials)

        search_request = {
            "pageSize": 10,
            "query": "https://www.nwhills.com/"
        }

        response = service.googleLocations().search(body=search_request).execute()

        googleLocations = response.get('googleLocations', None)

        # check if the return contains any data
        if googleLocations:
            for location in googleLocations:
                # write the data to a file
                with open('./output.json', 'w') as f:
                    f.write(json.dumps(location))

    except Exception as e:
        print(e)
        raise Exception(e)

if __name__ == "__main__":
    main()