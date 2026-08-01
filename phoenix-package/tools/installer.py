from datetime import datetime


class Installer:


    def install(self, package):

        print(
            datetime.now(),
            "- Installing",
            package
        )


if __name__ == "__main__":

    installer = Installer()

    installer.install(
        "phoenix-core"
    )