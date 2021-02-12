import requests
import pyodbc

database_connection = pyodbc.connect('Driver={SQL Server};'  # Defining connection to SQL database
                                     'Server=IMSISQLDEV.MAIN.IMSREPAIR.COM;'
                                     'Database=IMSIReportingDev;'
                                     'Trusted_Connection=yes;')

database_connection2 = pyodbc.connect('Driver={SQL Server};'  # Defining connection to SQL database
                                      'Server=IMSISQLDEV.MAIN.IMSREPAIR.COM;'
                                      'Database=IMSIReportingDev;'
                                      'Trusted_Connection=yes;')
cursor = database_connection.cursor()
cursor2 = database_connection2.cursor()
headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
           'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6IlNDT1BFX1JFQURfV1JJVEUiLCJpc3MiOiI1ZWE5OGViMjAzMzRiNzdkNWU2NGMxODgiLCJyZXNvdXJjZSI6IjVlOWRmNTM2NDQxMDZjNjVhYmY5OTM4MSIsImlhdCI6MTU4ODE3MDQzMn0.3ai7CdGbOEHUz3y1o0idTir09on7WGwGUoznDQ6ME2M'}
ActiveOnly = '{"status" : {"$in": ["STATUS_ACTIVE", "STATUS_ARCHIVED"] } }'

try:
    resource_url = 'https://api.hubplanner.com/v1/resource/search'  # Defining URL and Authorization for Get and Post requests
    api_data = requests.post(resource_url, headers=headers, data=ActiveOnly).json()

    for i in range(len(api_data)):
        agency = None
        number = None
        homestate = None
        onsite = None
        # print(api_data[i]["customFields"])
        _id = api_data[i]["_id"]
        email = api_data[i]["email"]
        updatedDate = api_data[i]["updatedDate"]
        if updatedDate is None:
            updatedDate = api_data[i]["createdDate"]
        fName = api_data[i]["firstName"]
        if fName.find("'") != -1:
            anomaly = fName.find("'")
            newFName = fName[:anomaly] + "'" + fName[anomaly:]
            fName = newFName
        lName = api_data[i]["lastName"]
        if lName.find("'") != -1:
            lanomaly = lName.find("'")
            newLName = lName[:lanomaly] + "'" + lName[lanomaly:]
            lName = newLName
        hStatus = api_data[i]["status"]
        for cfieldLen in range(len(api_data[i]["customFields"])):
            dId = api_data[i]["customFields"][cfieldLen]["templateId"]
            dType = api_data[i]["customFields"][cfieldLen]["templateType"]
            dLabel = api_data[i]["customFields"][cfieldLen]["templateLabel"]
            if api_data[i]["customFields"][cfieldLen]["templateLabel"] == "Employee ID":
                number = api_data[i]["customFields"][cfieldLen]["value"]
            if api_data[i]["customFields"][cfieldLen]["templateLabel"] == "Agency":
                if len(api_data[i]["customFields"][cfieldLen]["choices"]) > 0:
                    agency = api_data[i]["customFields"][cfieldLen]["choices"][0]["value"]
            if api_data[i]["customFields"][cfieldLen]["templateLabel"] == "Home State":
                if len(api_data[i]["customFields"][cfieldLen]["choices"]) > 0:
                    homestate = api_data[i]["customFields"][cfieldLen]["choices"][0]["value"]
            if api_data[i]["customFields"][cfieldLen]["templateLabel"] == "On-site Direct Report":
                if len(api_data[i]["customFields"][cfieldLen]["choices"]) > 0:
                    onsite = api_data[i]["customFields"][cfieldLen]["choices"][0]["value"]
            # sqlCommand2 = "Insert into Prep.IPOPsdimCustomFields (TemplateId, TemplateType, TemplateLabel) values(?,?,?);"
            values2 = [dId, dType, dLabel]
            # cursor.execute(sqlCommand2, values2)
            if api_data[i]["customFields"][cfieldLen]["templateType"] == "SELECT":
                if len(api_data[i]["customFields"][cfieldLen]["choices"]) > 0:
                    cValue = api_data[i]["customFields"][cfieldLen]["choices"][0]["value"]
                    cId = api_data[i]["customFields"][cfieldLen]["choices"][0]["choiceId"]
                    # sqlCommand3 = "Insert into Prep.IPOpsdimChoices (ChoiceId, Value, TemplateId) values(?,?,?);"
                    values3 = [cId, cValue, dId]
                    # cursor2.execute(sqlCommand3, values3)
            # cursor.commit()
            # cursor2.commit()
        # sqlCommand = "Insert into Prep.IPOpsdimEmployee " \
        #              "(ResourceId, EmailAddress, HPLastUpdatedDate, First_Name, Last_Name, HubPlannerStatus, Employee_number, Agency, HomeState, OnsiteSupervisor) " \
        #              "values(?,?,?,?,?,?,?,?,?,?);"
        values = [_id, email, updatedDate, fName, lName, hStatus, number, agency, homestate, onsite]
        # cursor.execute(sqlCommand, values)
        # cursor.commit()
except pyodbc.Error as err:
    # ErrorQuery = "INSERT INTO Log.Processing (Step, Description, Rows, EndDateTime, Duration) " \
    #              "VALUES ('Error in Employee Import Python', ?, 0, GETDATE(), '9999-12-31 23:59:59');"
    error = [err.args[1]]
    # cursor.execute(ErrorQuery, error)
    # cursor.commit()
