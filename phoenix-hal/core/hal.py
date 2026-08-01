import json
import os


class PhoenixHAL:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/device.json"
        )

        with open(path) as file:
            self.device = json.load(file)


    def get_device(self):

        return self.device["device"]


    def get_components(self):

        return self.device["components"]



if __name__ == "__main__":

    hal = PhoenixHAL()

    print("Phoenix HAL")
    print("----------------")

    print(
        hal.get_device()
    )

    print(
        hal.get_components()
    )