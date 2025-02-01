class Positron:
    def __init__(self):
        self.app = None
        self.t = 0
        self.total = 0

        self.page = 0

        # self.appsel = 0 #

        self._apps = [
            "GPIO"
        ]

    def tick(self):
        self.t += 1
        self.total += 1
        if self.total > 2 ** 16:
            self.total = 0

    def bootup(self):
        self.app = "bootup"
        self.t = 0

    def setapp(self, app : str):
        self.app = app
        self.t = 0
    def homescreen(self):
        self.app = None
        self.t = 0