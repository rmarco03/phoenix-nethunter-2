import json
import os


path = os.path.join(
    os.path.dirname(__file__),
    "../database/bootchain.json"
)


with open(path) as file:
    data = json.load(file)


print("Phoenix Boot Research Framework")
print("--------------------------------")

print("Device:")
print(data["device"])

print("\nBoot Chain:")

for stage in data["boot_chain"]:

    print(
        "-",
        stage["stage"],
        ":",
        stage["status"]
    )