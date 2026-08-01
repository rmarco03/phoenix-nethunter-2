import json
import os


class PhoenixPowerManager:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/power.json"
        )

        with open(path) as file:
            self.data = json.load(file)


    def get_components(self):

        return self.data["power"]


    def status(self):

        print("Phoenix Power Management")

        for component in self.data["power"]:
            print(
                component,
                ":",
                self.data["power"][component]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixPowerManager()

    manager.status()