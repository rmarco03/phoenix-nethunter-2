import os
import json
from datetime import datetime


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config():
    path = os.path.join(
        ROOT,
        "phoenix-env",
        "config",
        "project.json"
    )

    with open(path) as file:
        return json.load(file)


def create_build_folder():

    folder = os.path.join(ROOT, "build")

    if not os.path.exists(folder):
        os.makedirs(folder)


def write_log(message):

    log_folder = os.path.join(
        ROOT,
        "phoenix-env",
        "logs"
    )

    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(
        log_folder,
        "build.log"
    )

    with open(log_file, "a") as file:
        file.write(
            f"{datetime.now()} - {message}\n"
        )


def main():

    print("Phoenix Build System")
    print("--------------------")

    config = load_config()

    print(
        "Project:",
        config["project"]
    )

    print(
        "Version:",
        config["version"]
    )

    create_build_folder()

    write_log(
        "Build system executed"
    )

    print("Build preparation complete")


if __name__ == "__main__":
    main()