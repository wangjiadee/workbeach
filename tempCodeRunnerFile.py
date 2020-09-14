ser:
    def __init__(self,name):
        self.name = name

class VIPUser(User):
    def __init__(self,name,VIP_Level,start_Date,end_Date):
        super().__init__(name)
        # User.__init__(self.name)
        # super(VIPUser,self).__init__(bane)
        self.VIP_Level = VIP_Level
        self.start_Date = start_Date
        self.end_Date = end_Date
        
Tom = VIPUser('tom','VIP18','2020-02-02','2022-02-02')
print(Tom.__dict__)
        