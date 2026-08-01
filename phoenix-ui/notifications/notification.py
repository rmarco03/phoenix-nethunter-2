from datetime import datetime


class Notification:


    def send(self, message):

        print(
            datetime.now(),
            "[PHOENIX]",
            message
        )


if __name__ == "__main__":

    n = Notification()

    n.send(
        "Phoenix system started"
    )