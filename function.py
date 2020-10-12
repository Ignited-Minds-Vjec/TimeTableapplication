noOfDays = 5
periodCount = 6
timings = {}
links = {}
tt = []
readValue = ""
facultyCount = 8
facultyName = "IM"
link = ""
periodList = []


def get_key(val):
    for key, value in links.items():
        if val == value:
            return key


def details_collector():
    noOfDays = int(input("No of Working Days : "))
    periodCount = int(input("Period Count : "))
    for i in range(periodCount + 1):
        # Read the timings of the period and time of ending of the class in 24 hrs format
        readValue = input("Time "+str(i)+" : ")
        timings[i] = readValue+":00"
    # Add the number of teachers
    facultyCount = int(input("Faculty Count : "))
    for i in range(facultyCount):
        # Read teacher name or subject name
        facultyName = input("Faculty Name : ")
        # Read the link to the class
        link = input("Link : ")
        links[facultyName] = link
    for i in range(noOfDays):
        for j in range(periodCount):
            # Read the exact period name which is given above as key of links
            facultyName = input("Faculty Name : ")
            if facultyName in links.items():
                periodList.append(facultyName)
        tt.append(periodList)
        periodList.clear()
    config = open("Configuration_for_Timetable", "w")
    config.write(str(noOfDays))
    config.write("\n")
    config.write(str(periodCount))
    config.write("\n")
    config.write(str(timings))
    config.write("\n")
    config.write(str(links))
    config.write("\n")
    config.write(str(tt))
    config.close()


details_collector()