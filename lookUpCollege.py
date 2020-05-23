import requests
from bs4 import BeautifulSoup
import webbrowser
import NSAcolleges
import writeToFile

colleges = NSAcolleges.writeToCollege()
collegeInformation = {}

for state in colleges: 
    for college in colleges[state]:
        session = requests.Session()

        collegeName = college.lower().replace(" ", "-")
        # print(state + " " + college)
        response = session.get("https://www.collegesimply.com/colleges/" + state.lower() + "/" + collegeName)

        soup = BeautifulSoup(response.text, 'html.parser')
        information = soup.find(class_ = "col-12 col-md-8")

        if (information == None): # in case, it doesn't work for the future
            # print("failure") 
            continue
        else:
            parentInformation = information.find_parent()
            trList = parentInformation.findAll('tr') # further dive into all the information
            colList = parentInformation.findAll(class_ = "col-12 col-md-6") + parentInformation.findAll(class_ = "col-12 col-md-8")
            totalInfo = []
            for i in colList:
                nameList = i.findAll(class_ = 'card-title text-uppercase text-muted mb-2')
                if (nameList != None):
                    valueList = i.findAll(class_ = 'display-3')
                    if valueList == None: value = i.findAll(class_ = 'display-3 mb-0')
                    for name, value in zip(nameList[1:], valueList[1:]):
                        if (name.get_text().strip() not in ['Admission Standards', 'Bachelor\'s Degrees Graduation Rate', 'Average Salary After 10 Years']):
                            # print(name.get_text().strip() + " : " + value.get_text().strip())
                            totalInfo.append(name.get_text().strip() + " : " + value.get_text().strip())
            for tr in trList:
                tdList = tr.findAll('td')
                inState = False
                for tdIndex in range(0, len(tdList) - 1, 2): # printing out all the information
                    name = tdList[tdIndex].get_text()
                    if name in ['SAT', 'GPA', 'On Campus Housing', 'Applicant Competition']:
                        value = tdList[tdIndex+1].get_text()
                        # print(name + ' : ' + value)
                        totalInfo.append(name + " : " + value)
            collegeInformation[college] = totalInfo

            # for info in collegeInformation:
            #     print(info + " : " + collegeInformation[info])

# print(collegeInformation.keys())

newCollegeList = {}
# print(colleges.keys())
for state in colleges: 
    totalInfomation = {}
    for college in colleges[state]:
        if college in list(collegeInformation.keys()):
            information = collegeInformation[college]
            totalInfomation[college] = information
    newCollegeList[state] = totalInfomation

writeToFile.writeToCollege(newCollegeList)
# print(newCollegeList.keys())
# print(newCollegeList["Colorado"].keys())
# print(newCollegeList["Colorado"])
# print()
# print(colleges["Colorado"])