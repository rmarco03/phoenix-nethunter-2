import json
import os


class PhoenixPackageManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/packages.json"
        )

        with open(path) as file:
            self.packages = json.load(file)


    def list_packages(self):

        return self.packages["packages"]


    def install(self, package):

        if package in self.packages["packages"]:

            self.packages["packages"][package]["status"] = "installed"

            print(
                package,
                "installed"
            )

        else:

            print(
                "Package not found"
            )


    def remove(self, package):

        if package in self.packages["packages"]:

            self.packages["packages"][package]["status"] = "removed"

            print(
                package,
                "removed"
            )


    def show(self):

        print("Phoenix Package Manager")
        print("-----------------------")

        for package in self.packages["packages"]:

            print(
                package,
                ":",
                self.packages["packages"][package]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixPackageManager()

    manager.show()