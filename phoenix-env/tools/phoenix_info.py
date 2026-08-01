import json

print("Phoenix NetHunter Development Environment")
print("---------------------------------------")

with open("../config/project.json") as file:
    project = json.load(file)

print("Project:", project["project"])
print("Version:", project["version"])
print("Target:", project["target_device"])
print("Architecture:", project["architecture"])