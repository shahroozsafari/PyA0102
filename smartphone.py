
class Phone:
    def __init__(self, body, display, platfrom, memory, camera):
        self.body = body
        self.display = display
        self.platform = platfrom
        self.memory = memory
        self.camera = camera


class Samsung(Phone):
    brand = "Samsung"
    def __init__(self, model,body, display, platfrom, memory, camera):
        super().__init__(body, display, platfrom, memory, camera)
        self.model = model

class Apple(Phone):
    brand = "Apple"
    def __init__(self, model,body, display, platfrom, memory, camera):
        super().__init__(body, display, platfrom, memory, camera)
        self.model = model

#---------------- Main -------------
body={"dim":[160,77,8] , "weight":240,"sim":"nano sim" }
display = {"type":"LTPO","size":6.7}
platfrom ={}
memory = {}
camera = {}

phone1 = Phone(body,display,platfrom,memory,camera)
s23 = Samsung("S23 Ultra",body,display,platfrom,memory,camera)
print(s23.body["weight"],"gr")
