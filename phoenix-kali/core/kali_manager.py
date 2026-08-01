import json
import os


class PhoenixKaliManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/kali.json"
        )

        with open(path) as file:
            self.kali = json.load(file)


    def show_status(self):

        print(
            "Phoenix Kali Integration"
        )

        print(
            "-----------------------"
        )

        for item in self.kali["kali"]:

            print(
                item,
                ":",
                self.kali["kali"][item]
            )


if __name__ == "__main__":

    manager = PhoenixKaliManager()

    manager.show_status()