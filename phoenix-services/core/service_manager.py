import json
import os


class PhoenixServiceManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/services.json"
        )

        with open(path) as file:
            self.services = json.load(file)


    def list_services(self):

        return self.services["services"]


    def start_service(self, name):

        if name in self.services["services"]:

            self.services["services"][name]["status"] = "running"


    def stop_service(self, name):

        if name in self.services["services"]:

            self.services["services"][name]["status"] = "stopped"


    def show_status(self):

        print("Phoenix Service Manager")
        print("----------------------")

        for service in self.services["services"]:

            print(
                service,
                ":",
                self.services["services"][service]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixServiceManager()

    manager.start_service("network")

    manager.show_status()