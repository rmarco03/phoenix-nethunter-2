import json
import os


class PhoenixUIManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/ui.json"
        )

        with open(path) as file:
            self.config = json.load(file)


    def show_config(self):

        print("Phoenix UI Framework")
        print("--------------------")

        interface = self.config["interface"]

        for item in interface:

            print(
                item,
                ":",
                interface[item]
            )


if __name__ == "__main__":

    ui = PhoenixUIManager()

    ui.show_config()