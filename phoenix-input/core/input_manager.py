import json
import os


class PhoenixInputManager:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/input.json"
        )

        with open(path) as file:
            self.inputs = json.load(file)


    def list_inputs(self):

        return self.inputs["inputs"]


    def get_status(self, name):

        return self.inputs["inputs"][name]["status"]



if __name__ == "__main__":

    manager = PhoenixInputManager()

    print("Phoenix Input Framework")
    print("-----------------------")

    for item in manager.list_inputs():

        print(
            item,
            ":",
            manager.get_status(item)
        )