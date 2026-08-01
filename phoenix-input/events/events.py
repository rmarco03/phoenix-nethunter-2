from datetime import datetime


class InputEvent:

    def __init__(self, source, action):

        self.source = source
        self.action = action
        self.time = datetime.now()


    def show(self):

        print(
            f"{self.time} | {self.source} | {self.action}"
        )



if __name__ == "__main__":

    event = InputEvent(
        "touchscreen",
        "tap"
    )

    event.show()