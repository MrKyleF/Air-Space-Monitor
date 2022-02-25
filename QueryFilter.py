#Kyle R Fogerty
#QueryFilter: Contains Parameters required to perform filtering

class QueryFilter:
    def setKeywords(self):
        if self.category == "miltary":
            self.keywords = ["force", "army","navy","unit "]
        else:
            self.keywords = []
        

    def __init__(self, category="miltary"):
        self.category = category