





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


