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

    
    def newItem(itemDescription):

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
            id = response.json("id")
            title = response.json("name")
            status = response.json("idList")
            dateLastAction = response.json("dateLastAction")


    def __str__(self):
        return 'id: ' + self.id + ', idList: ' + self.idList + ', name: ' + self.name + ', datelastactivity: ' + self.dateLastActivity 

