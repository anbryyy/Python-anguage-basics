import time


class TrafficLight:

    def running(self):
        while True:
            self.__color = "red"
            print(f"{self.__color}")
            time.sleep(7)
            self.__color = "yellow"
            print(f"{self.__color}")
            time.sleep(2)
            self.__color = "green"
            print(f"{self.__color}")
            time.sleep(7)

t = TrafficLight()
t.running()