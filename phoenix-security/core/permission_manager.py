class PermissionManager:


    def __init__(self):

        self.permissions = {}


    def add_permission(
        self,
        service,
        permission
    ):

        self.permissions[service] = permission


    def check_permission(
        self,
        service
    ):

        return self.permissions.get(
            service,
            None
        )


if __name__ == "__main__":

    manager = PermissionManager()

    manager.add_permission(
        "network",
        "allowed"
    )

    print(
        manager.check_permission(
            "network"
        )
    )