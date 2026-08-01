class ResourceManager:


    def __init__(self):

        self.resources = {

            "cpu": "managed",
            "memory": "managed",
            "storage": "managed"

        }


    def status(self):

        return self.resources



if __name__ == "__main__":

    manager = ResourceManager()

    print(
        manager.status()
    )