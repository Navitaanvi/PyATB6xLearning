from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def SetGear(self):
        pass

class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine,GearBox):

    def start(self):
        print("Starting ")

    def stop(self):
        print("stop")

    def SetGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.SetGear()
        self.stop()

tesla = Car()
tesla.drive()


