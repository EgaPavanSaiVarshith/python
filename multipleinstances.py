class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_call(self,number):
        print("calling..{}".format(number))

mobile_obj1 = Mobile("iPhone 12 Pro", "12 MP")
print(id(mobile_obj1))
mobile_obj2 = Mobile("Galaxy M51", "64 MP")
print(id(mobile_obj2))
