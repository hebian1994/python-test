from email import header
from urllib import request
from pip import main
import requests
import json


def getKeyVaultToken(url):
    headers = {
        'Metadata': 'true'
    }
    r = requests.request("GET", url, headers=headers)
    info = r.text
    return json.loads(info)['access_token']


def getKeyVaultSecretValue(access_token, keyVaultName, secretName):
    urlKeyVaultUrl = "https://"+keyVaultName + \
        ".vault.azure.net/secrets/"+secretName+"?api-version=2016-10-01"
    # urlKeyVaultUrl = "http://localhost:9999/getValue"
    headers = {
        'Authorization': "Bearer "+access_token
    }
    r = requests.request("GET", urlKeyVaultUrl, headers=headers)
    info = r.text
    return json.loads(info)['value']


def main():
    # url="http://localhost:9999/getToken"
    url = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net"
    token = getKeyVaultToken(url)
    value = getKeyVaultSecretValue(token, "mykv0614", "test0617")
    print(value)


if __name__ == '__main__':
    main()
