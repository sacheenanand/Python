__author__ = 'sanand'

import csv

with open("Adde.csv", "w", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["Products", "Yes", "No"])
    data_handler.writerow(["Bamboo", "Yes"])
    data_handler.writerow(["Bitbucket","Yes"])
    data_handler.writerow(["Browser Stack","Yes"])
    data_handler.writerow(["BugZilla"," ","No"])
    data_handler.writerow(["Citrix GoToMeeting","Yes"])
    data_handler.writerow(["Confluence","yes"])
    data_handler.writerow(["CVS"," ","No"])
    data_handler.writerow(["Jira","Yes"])
    data_handler.writerow(["Jira Service Desk","Yes"])
    data_handler.writerow(["IntelliJ","Yes"])
    data_handler.writerow(["Lastpass","Yes"])
    data_handler.writerow(["Microsoft Office","Yes"])
    data_handler.writerow(["Mitel","Yes"])
    data_handler.writerow(["Sales Force","Yes"])
    data_handler.writerow(["Verizon Phone"," ","No"])
    data_handler.writerow(["VPN","Yes"])
    data_handler.writerow(["Wiki"," ","No"])
    data_handler.writerow(["Laptop"," ","No"])
    data_handler.writerow(["Laptop","Mac OS X"])







