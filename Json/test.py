import json

with open("example.json", "r") as f:
    date=json.load(f)

print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

#Dn_values
print(date["imdata"][0]["l1PhysIf"]["attributes"]["dn"],"                            ",date["imdata"][0]["l1PhysIf"]["attributes"]["speed"]," ",date["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])

print(date["imdata"][1]["l1PhysIf"]["attributes"]["dn"],"                            ",date["imdata"][1]["l1PhysIf"]["attributes"]["speed"]," ",date["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])

print(date["imdata"][2]["l1PhysIf"]["attributes"]["dn"],"                            ",date["imdata"][2]["l1PhysIf"]["attributes"]["speed"]," ",date["imdata"][2]["l1PhysIf"]["attributes"]["mtu"])







