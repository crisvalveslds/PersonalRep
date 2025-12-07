with open("courses.txt") as courses_file:
    for line in courses_file:
        print(line.strip().split())
