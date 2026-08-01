import json
import os


class PhoenixContainerManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/containers.json"
        )

        with open(path) as file:
            self.containers = json.load(file)


    def list_containers(self):

        return self.containers["containers"]


    def start(self, name):

        if name in self.containers["containers"]:

            self.containers["containers"][name]["status"] = "running"


    def stop(self, name):

        if name in self.containers["containers"]:

            self.containers["containers"][name]["status"] = "stopped"


    def show(self):

        print("Phoenix Container Manager")
        print("------------------------")

        for container in self.containers["containers"]:

            print(
                container,
                ":",
                self.containers["containers"][container]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixContainerManager()

    manager.show()