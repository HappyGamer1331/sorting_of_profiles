profiles = [['Rose Winds', 'Clouds Computing', 'USA', 6.5, 5000, 5, 'F'],
            ['Merry Brown', 'Clouds Computing', 'UK', 5, 7000, 5, 'F'],
            ['Lina Mesro', ' Cyber Security', 'Malaysia', 7, 6500, 4, 'F'],
            ['Abdul Fazil', 'Big Data', 'Australia', 11, 8000, 4, 'M'],
            ['Chris Janes', 'Big Data', 'Ireland', 7, 2500, 4, 'M'],
            ['Sireen May', 'Artificial Intelligence', 'Australia', 0, 4000, 4, 'F'],
            ['Jine Tims', 'Robotics', 'Australia', 0, 3500, 3, 'M'],
            ['Niki Rohdes', 'Artificial Intellignence', 'China', 9, 8500, 5, 'F']]

def alphabetical_sort():
    global profiles
    profiles.sort()
    for profile in profiles:
        print(profile)

def experience_sort():
    global profiles
    cur_number = 0
    profiles.sort()
    sorted_profiles = profiles
    profiles = []
    nums = []
    length = len(sorted_profiles)
    for num in range(length):
        number = sorted_profiles[num][3]
        nums.append((number,num))
        nums.sort(reverse= True)
    for a in range(length):
        profiles.append(sorted_profiles[nums[a][1]])
    for profile in profiles:
        print(profile)

def salary_sort():
    global profiles
    cur_number = 0
    profiles.sort()
    sorted_profiles = profiles
    profiles = []
    nums = []
    length = len(sorted_profiles)
    for num in range(length):
        number = sorted_profiles[num][4]
        nums.append((number,num))
        nums.sort()
    for a in range(length):
        profiles.append(sorted_profiles[nums[a][1]])
    for profile in profiles:
        print(profile)

print("The Following List Is Sorted Based On Alphabetical Order (A-Z)")
alphabetical_sort()

print("The Following List Is Sorted Based On Salary (Low To High)")
salary_sort()

print("The Following List Is Sorted Based On Experience (High To Low)")
experience_sort()
