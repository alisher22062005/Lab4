import json

with open("example.json", "r") as f:
    date=json.load(f)
"""a=(date["imdata"][0]["l1PhysIf"]["attributes"]["dn"])
all1=date["imdata"][0]["l1PhysIf"]["attributes"]
ALL=date["imdata"]
g=0"""

print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

#Dn_values
for i in date["imdata"][0]["l1PhysIf"]["attributes"] :
    if i=="dn":
        print(date["imdata"][0]["l1PhysIf"]["attributes"]["dn"],"                            ",date["imdata"][0]["l1PhysIf"]["attributes"]["speed"]," ",date["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])


for i in date["imdata"][1]["l1PhysIf"]["attributes"] :
    if i=="dn":
        print(date["imdata"][1]["l1PhysIf"]["attributes"]["dn"],"                            ",date["imdata"][1]["l1PhysIf"]["attributes"]["speed"]," ",date["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])


for i in date["imdata"][2]["l1PhysIf"]["attributes"] :
    if i=="dn":
        print(date["imdata"][2]["l1PhysIf"]["attributes"]["dn"],"                            ",date["imdata"][2]["l1PhysIf"]["attributes"]["speed"]," ",date["imdata"][2]["l1PhysIf"]["attributes"]["mtu"])







