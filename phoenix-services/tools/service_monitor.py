from datetime import datetime


class ServiceMonitor:


    def log(self, service, status):

        print(
            datetime.now(),
            "|",
            service,
            "|",
            status
        )


if __name__ == "__main__":

    monitor = ServiceMonitor()

    monitor.log(
        "network",
        "running"
    )