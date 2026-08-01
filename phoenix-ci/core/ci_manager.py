import json
import os


class PhoenixCIManager:


    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../config/pipeline.json"
        )

        with open(path) as file:
            self.pipeline = json.load(file)


    def show_pipeline(self):

        print(
            "Phoenix CI/CD Framework"
        )

        print(
            "----------------------"
        )

        for item in self.pipeline["pipeline"]:

            print(
                item,
                ":",
                self.pipeline["pipeline"][item]["enabled"]
            )


if __name__ == "__main__":

    ci = PhoenixCIManager()

    ci.show_pipeline()