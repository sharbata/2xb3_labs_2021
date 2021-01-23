def are_valid_groups(student_nums, groups):
    students_in_groups = []
    for i in range(len(groups)):
        for j in groups[i]:
            students_in_groups.append(j)

    for i in student_nums:
        if(not(i in students_in_groups)):
            return False
    
    return True
           

## Toronto Raptors = We the South
## YOU MAD BRO?
nums = [12, 13, 14, 16, 18, 821, 763, 290, 27723, 25267]
groups = [[12, 821, 763], [13, 14, 290], [16, 18, 27723]]

print(are_valid_groups(nums, groups))
