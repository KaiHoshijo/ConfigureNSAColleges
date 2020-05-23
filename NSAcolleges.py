import requests
from bs4 import BeautifulSoup

# requests to the NSA recommended college
response = requests.get('https://www.iad.gov/NIETP/reports/cae_designated_institutions.cfm', verify = False)

# getting the web scrap of it
soup = BeautifulSoup(response.text, 'html.parser')

target = "CAE-CD"
colleges = {}

stateTables = soup.findAll("table")

def assignToCollege(Rows):
    stateColleges = []
    for row in Rows:
        collegeName = row.find("a").get_text()
        designations = row.findAll("li")
        for designation in designations:
            certificate = designation.get_text().split(" ")[0]
            if certificate == target:
                stateColleges.append(collegeName)
    return stateColleges

def writeToCollege():
    for state in stateTables:
        # getting the different rows of it
        oddRows = state.findAll(class_ = "oddRow")
        evenRows = state.findAll(class_ = "evenRow")
        totalRows = []
        for row in range(len(oddRows)):
            totalRows.append(oddRows[row])
            if (row < len(evenRows)):
                totalRows.append(evenRows[row])

        # assigning colleges depending on each row
        stateColleges = assignToCollege(totalRows)

        # appending colleges depending on college
        colleges[state.find("caption").get_text()] = stateColleges
    return colleges

#print(" ".join(list(colleges.keys())))
# print(colleges["Colorado"])




