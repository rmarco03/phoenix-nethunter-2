from datetime import datetime


class AuditLogger:


    def write(self, event):

        timestamp = datetime.now()

        print(
            timestamp,
            "| SECURITY EVENT |",
            event
        )


if __name__ == "__main__":

    logger = AuditLogger()

    logger.write(
        "Security framework initialized"
    )