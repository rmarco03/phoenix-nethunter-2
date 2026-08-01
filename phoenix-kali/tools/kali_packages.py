class KaliPackageBridge:


    def __init__(self):

        self.packages = []


    def add(self, package):

        self.packages.append(package)


    def list(self):

        return self.packages



if __name__ == "__main__":

    bridge = KaliPackageBridge()

    bridge.add(
        "kali-tools"
    )

    print(
        bridge.list()
    )