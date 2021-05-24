#Class Object for Trello Item
import requests
import os

trello_key = os.environ.get('TRELLO_KEY')
trello_token = os.environ.get('TRELLO_TOKEN')
listtodo = os.environ.get('LISTTODO')

class Item:

    def __init__(self, id, idList, name, dateLastActivity ):
        self.id = id
        self.idList = idList
        self.name = name
        self.dateLastActivity = dateLastActivity

    
    def createItemInTrello(itemDescription):

        url = "https://api.trello.com/1/cards"

        query = {
            'key': trello_key,
            'token': trello_token,
            'idList': listtodo,
            'name': itemDescription
            }

        response = requests.request(
            "POST",
            url,
            params=query
            )
        #valid response received
        if response.status_code == 200:
            
            jsonResponse = response.json()
            id = jsonResponse["id"]
            name = jsonResponse["name"]
            idList = jsonResponse["idList"]
            dateLastActivity = jsonResponse["dateLastActivity"]


    def __str__(self):
        return 'id: ' + self.id + ', idList: ' + self.idList + ', name: ' + self.name + ', datelastactivity: ' + self.dateLastActivity 

