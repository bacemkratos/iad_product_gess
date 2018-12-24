





class Product:
     name = ""
     type =  ""
     producer = ""
     details = {}

     def __init__(self,name,type,producer,components) -> None:
          super().__init__()
          self.name = name
          self.type = type
          self.producer=producer
          self.details=components

     def __str__(self):
          return str(self.__dict__)

     def __eq__(self, other):
           return self.__dict__ == other.__dict__



