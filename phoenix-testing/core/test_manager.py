import json
import os


class PhoenixTestManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../database/tests.json"
        )

        with open(path) as file:
            self.tests = json.load(file)


    def list_tests(self):

        return self.tests["tests"]


    def run_test(self, name):

        if name in self.tests["tests"]:

            print(
                "Running test:",
                name
            )

            self.tests["tests"][name]["status"] = "completed"


    def show(self):

        print("Phoenix Hardware Testing Framework")
        print("----------------------------------")

        for test in self.tests["tests"]:

            print(
                test,
                ":",
                self.tests["tests"][test]["status"]
            )


if __name__ == "__main__":

    manager = PhoenixTestManager()

    manager.show()