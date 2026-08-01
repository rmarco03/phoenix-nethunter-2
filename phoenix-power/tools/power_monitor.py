from datetime import datetime


class PowerMonitor:


    def log(self, event):

        time = datetime.now()

        print(
            time,
            "-",
            event
        )


if __name__ == "__main__":

    monitor = PowerMonitor()

    monitor.log(
        "Power monitoring started"
    )