from datetime import datetime


class TestRunner:


    def run(self, test):

        print(
            datetime.now(),
            "- Running:",
            test
        )


if __name__ == "__main__":

    runner = TestRunner()

    runner.run(
        "Phoenix Hardware Tests"
    )