
def are_valid_groups(student_nums, groups):
    students_in_groups = []
    #adds student numbers in all groups to one list of strings
    for i in range(len(groups)):
        for j in groups[i]:
            students_in_groups.append(j)

    #checks if all groups are only of size 2 or 3
    for i in groups:
        if len(i) < 2 or len(i) > 3:
            return False
    #print("group size passed")

    #check if student number is in a group and only occurs once between all groups
    for i in student_nums:
        if(not(i in students_in_groups)):
            #print("doesn't exist")
            return False
        if(i in students_in_groups):
            students_in_groups.remove(i)
        if(i in students_in_groups):
            #print("occured again")
            return False

    return True

#comment
#YOU MAD EH DO YOU EVEN LIFT? 


nums = ["12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
groups = [["12", "13", "11",], ["14", "15", "16"], ["17", "18"], ["19", "20", "21"], ["22", "23", "24"]]
print(nums)
print(groups)
