import json
import os


class PhoenixNetworkManager:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/network.json"
        )

        with open(path) as file:
            self.network = json.load(file)


    def list_interfaces(self):

        return self.network["interfaces"]


    def show_status(self):

        print("Phoenix Network Framework")
        print("-------------------------")

        for interface in self.network["interfaces"]:

            print(
                interface,
                ":",
                self.network["interfaces"][interface]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixNetworkManager()

    manager.show_status()