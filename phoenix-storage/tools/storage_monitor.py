from datetime import datetime


class StorageMonitor:


    def log(self, event):

        print(
            datetime.now(),
            "-",
            event
        )


if __name__ == "__main__":

    monitor = StorageMonitor()

    monitor.log(
        "Storage monitoring initialized"
    )