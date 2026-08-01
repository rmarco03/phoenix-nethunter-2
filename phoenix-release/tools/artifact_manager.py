from datetime import datetime


class ArtifactManager:


    def create(self, name):

        print(
            datetime.now(),
            "- Creating artifact:",
            name
        )


if __name__ == "__main__":

    manager = ArtifactManager()

    manager.create(
        "phoenix-development-build"
    )