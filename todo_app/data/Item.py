#Class Object for Trello Item
import requests
import os

trello_key = os.environ.get('TRELLO_KEY')
trello_token = os.environ.get('TRELLO_TOKEN')
listtodo = os.environ.get('LISTTODO')


class Item:

    def __init__(self, id, status, title,datelastaction ):
        self.id = id
        self.status = status
        self.title = title
        self.datelastaction = datelastaction

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def dateLastAction(self):
        return self._dateLastAction

    @dateLastAction.setter
    def id(self, value):
        self._id = value


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
        return 'id: ' + self.id + ', status: ' + self.status + ', title: ' + self.title + ', datelastaction: ' + self.datelastaction 



    