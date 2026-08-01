import json
import os


path = os.path.join(
    os.path.dirname(__file__),
    "../config/kernel.json"
)


with open(path) as file:
    kernel = json.load(file)


print("Phoenix Kernel Framework")
print("------------------------")

print(
    "Kernel:",
    kernel["kernel"]["name"]
)

print(
    "Architecture:",
    kernel["kernel"]["architecture"]
)

print(
    "Target:",
    kernel["kernel"]["target"]
)

print(
    "Status:",
    kernel["kernel"]["status"]
)