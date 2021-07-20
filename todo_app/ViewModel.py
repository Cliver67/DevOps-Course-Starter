
class ViewModel:

    def __init__(self, items, todo, doing, done):
        self._items = items
        self._todo = todo
        self._doing = doing
        self._done = done
        #self._showtodo = showtodo
        #self._showdoing = showdoing
        #self._showdone = showdone

    #returned cards from API call to Trello
    @property
    def items(self):
        #
        
        #if (self.showtodo == True):
        #    self.todo_items()
        
        #if (self.showdoing ==True):
        #    self.doing_items()

        #if (self.showdone ==True):
        #    self.done_items(self._done )
        
        #self._items == displaylist()
        #change this to show new items i.e filtered based on showxx
        return self._items

    #Key values for columns
    @property
    def todo(self):
        return self._todo

    @property
    def doing(self):
        return self._doing

    @property
    def done(self):
        return self._done

    #proporties to control which categories to display
    @property
    def showdone(self):
        return self._showdone
    @property
    def showtodo(self):
        return self._showtodo
    @property
    def showdoing(self):
        return self._showdoing

    

    #methods to control what to return
    @property
    def done_items (self):
        #return only items that are in the Done list
        #consider last update date later on
        displaylist = []
        for x in self._items:
            if(x.idList == self._done):
                #filter match
                displaylist.append(x)
                
        return displaylist

    def doing_items():
         #return only items that are in the Done list
        
        return 0

    def todo_items():
        #return only items that are in the Done list
        
        return 0       
