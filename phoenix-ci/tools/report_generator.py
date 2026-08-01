from datetime import datetime


class ReportGenerator:


    def create(self, message):

        print(
            datetime.now(),
            "| REPORT |",
            message
        )


if __name__ == "__main__":

    report = ReportGenerator()

    report.create(
        "Build completed"
    )