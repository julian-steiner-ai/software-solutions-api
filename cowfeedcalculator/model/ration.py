class Ration:
    def __init__(self, name, count):
        self.name = name
        self.count = count
    
    def to_json(self):
        return self.__dict__