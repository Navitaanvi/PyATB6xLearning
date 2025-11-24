from abc import ABC,abstractmethod

class EcxelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(EcxelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("Reading from Excel file")

    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1 = TC1()
tc1.runTC()
