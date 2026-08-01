import json
import os


class PhoenixStorageManager:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/storage.json"
        )

        with open(path) as file:
            self.storage = json.load(file)


    def list_components(self):

        return self.storage["storage"]


    def show_status(self):

        print("Phoenix Storage Framework")
        print("-------------------------")

        for item in self.storage["storage"]:

            print(
                item,
                ":",
                self.storage["storage"][item]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixStorageManager()

    manager.show_status()