import json
import os


class PhoenixReleaseManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../config/version.json"
        )

        with open(path) as file:
            self.version = json.load(file)


    def get_version(self):

        v = self.version["version"]

        return (
            f'{v["major"]}.'
            f'{v["minor"]}.'
            f'{v["patch"]}'
        )


    def show(self):

        print(
            "Phoenix Release Manager"
        )

        print(
            "Version:",
            self.get_version()
        )

        print(
            "Channel:",
            self.version["channel"]
        )


if __name__ == "__main__":

    manager = PhoenixReleaseManager()

    manager.show()