from datetime import datetime


class ContainerRuntime:


    def launch(self, container):

        print(
            datetime.now(),
            "- Starting container:",
            container
        )


    def shutdown(self, container):

        print(
            datetime.now(),
            "- Stopping container:",
            container
        )


if __name__ == "__main__":

    runtime = ContainerRuntime()

    runtime.launch(
        "kali-arm64"
    )