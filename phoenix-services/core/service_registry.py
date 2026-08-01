class ServiceRegistry:


    def __init__(self):

        self.registry = {}


    def register(
        self,
        name,
        module
    ):

        self.registry[name] = module


    def list(self):

        return self.registry



if __name__ == "__main__":

    registry = ServiceRegistry()

    registry.register(
        "network",
        "Phoenix Network Framework"
    )

    print(
        registry.list()
    )