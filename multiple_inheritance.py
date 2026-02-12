class Framework:
    def __init__(self):
        self.db: dict[str, int] = {}

    def render(self): print("render framework")
    def activate(self): print("activate framework")

class Plugin:
    def __init__(self):
        self.cookies: list[str] = []
    
    def render(self): print("render plugin")
    def activate(self): print("activate plugin")

class Website(Framework, Plugin):
    def activate(self):
        return Plugin.activate(self)

class Service(Framework, Plugin):
    def __init__(self):
        Plugin.__init__(self)
    def render(self):
        Plugin.render(self)
    
site = Website()
print(site.db)
site.render()
site.activate()

service = Service()
print(service.cookies)
service.render()
service.activate()