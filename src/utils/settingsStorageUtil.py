class StorageUtil:
    def __init__(self):
        self.path = "settings.txt"
        self.buffer_data = []
        self.load()
    
    def load(self):
        with open(self.path, 'r') as f:
            self.buffer_data = f.read().splitlines()
            
    def setIp(self, ip):
        self.buffer_data[0] = ip
        self.save()

    def save(self):
        with open(self.path, 'w') as f:
           for line in self.buffer_data:
               f.write(f'''{line}\n''')
        
    def setPort(self, port):
        self.buffer_data[1] = port
        self.save()

    def setMode(self, mode):
        self.buffer_data[2] = mode
        self.save()

    def setActivate(self, activate):
        self.buffer_data[3] = activate
        self.save()

    def setHeight(self, height):
        self.buffer_data[4] = height
        self.save()

    def getIp(self):
        return self.buffer_data[0]
    
    def getPort(self):
        return self.buffer_data[1]
    
    def getMode(self):
        return self.buffer_data[2]
    
    def getActivate(self):
        return self.buffer_data[3]
    
    def getHeight(self):
        return self.buffer_data[4]
    
    def create(self):
        with open(self.path, 'w') as f:
            f.write(f"000.000.0.00\n0000\n1\nTrue\n100\n")

    def check(self):
        with open(self.path, 'r') as f:
            self.buffer_data = f.read().splitlines()
        if len(self.buffer_data) != 5:
            self.create()
            self.load()
