import json
import os


class PhoenixSecurityManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/security.json"
        )

        with open(path) as file:
            self.security = json.load(file)


    def list_features(self):

        return self.security["security"]


    def show_status(self):

        print("Phoenix Security Framework")
        print("--------------------------")

        for item in self.security["security"]:

            print(
                item,
                ":",
                self.security["security"][item]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixSecurityManager()

    manager.show_status()