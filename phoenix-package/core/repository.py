class Repository:


    def __init__(self):

        self.packages = []


    def add(self, package):

        self.packages.append(package)


    def list(self):

        return self.packages



if __name__ == "__main__":

    repo = Repository()

    repo.add(
        "phoenix-network"
    )

    print(
        repo.list()
    )