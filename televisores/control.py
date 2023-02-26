class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.control = self

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

