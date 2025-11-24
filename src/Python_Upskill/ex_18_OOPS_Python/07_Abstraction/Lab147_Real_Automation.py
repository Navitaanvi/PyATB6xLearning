from abc import ABC,abstractmethod

class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop Command ")

class ChromeBrowser(BrowserManager):

    def start(self):
        print("We are starting chrome ")

tc = ChromeBrowser()
tc.start()
tc.stop()

