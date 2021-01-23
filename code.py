def are_valid_groups(studentList, groupList):
    numOfGroups = len(groupList)
    groupSize = len(groupList[0])
    if (groupSize != len(studentList)):
        #print("More student numbers than the number of members in each group")
        return False 
    valids = 0
    for groupNum in range(numOfGroups):
        for groupMem in range(groupSize):
            if (studentList[groupMem] != groupList[groupNum][groupMem] and groupNum == numOfGroups - 1):
                #print ("groups are not valid")
                return False
            elif (studentList[groupMem] == groupList[groupNum][groupMem]):
                #print ("valid member")
                valids = valids + 1
                if (valids == groupSize - 1):
                    #print ("atleast one group is valid")
                    return True


studentList = [1,2,3,4]
groupList = [[5,2,3,4], [1,2,3,4]]

are_valid_groups(studentList, groupList)