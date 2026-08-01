from datetime import datetime


class NetworkMonitor:


    def event(self, message):

        print(
            datetime.now(),
            "-",
            message
        )


if __name__ == "__main__":

    monitor = NetworkMonitor()

    monitor.event(
        "Network monitoring started"
    )