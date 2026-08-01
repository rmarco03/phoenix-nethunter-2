from datetime import datetime


class HardwareReport:


    def generate(self, component, result):

        print(
            datetime.now(),
            "|",
            component,
            "|",
            result
        )


if __name__ == "__main__":

    report = HardwareReport()

    report.generate(
        "CPU",
        "Detected"
    )