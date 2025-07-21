#---------------------------While Loop in Python------------------------------------

# cnt = 1
# while (cnt < 3):
#     cnt = cnt + 1
#     print("Hello")

#-------------------------Using else statement with While Loop------------------------

# cnt = 0
# while (cnt < 3):
#     cnt = cnt + 1
#     print("Hello")
# else:
#     print("From Else Block")

#-------------------------Infinite While Loop--------------------------------

# count = 0
# while (count==0):
#     print("infinite")

#-------------------------For Loop--------------------------------------------

# n = 4
# for i in range(0, n):
#     print(i)

#-----------------------------List, Tuple, String, and Dictionary Iteration Using for Loops-----------------------------

# li = ["god", "of", "war"]
# for i in li:
#     print(i)
    
# tup = ("god", "of", "war")
# for i in tup:
#     print(i)
    
# s = "God"
# for i in s:
#     print(i)
    
# d = dict({'x':123, 'y':354})
# for i in d:
#     print("%s  %d" % (i, d[i]))
    
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i),

#---------------------------------------------------------------------------------------

# def calculate_grade(avg):
#     if avg >= 90:
#         return "A+"
#     elif avg >= 80:
#         return "A"
#     elif avg >= 70:
#         return "B"
#     elif avg >= 60:
#         return "C"
#     else:
#         return "F"


# def add_student():
#     name = input("Enter student's name: ")
#     subjects = ["Math", "Science", "English"]
#     marks = {}

#     for subject in subjects:
#         score = int(input(f"Enter marks for {subject}: "))
#         marks[subject] = score

#     total = sum(marks.values())
#     avg = total / len(subjects)
#     grade = calculate_grade(avg)

#     with open("report_cards.txt", "a") as f:
#         f.write(f"{name} | Total: {total} | Average: {avg:.2f} | Grade: {grade}\n")

#     print("Report saved!")

# def view_reports():
#     try:
#         with open("report_cards.txt", "r") as f:
#             print("\nSaved Report Cards:")
#             print(f.read())
#     except FileNotFoundError:
#         print("No reports found yet.")

# # Main menu
# while True:
#     print("\n1. Add Report  2. View Reports  3. Exit")
#     choice = input("Choose an option: ")

#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         view_reports()
#     elif choice == "3":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Try again.")

#-------------------------------------------------------------------------------------------------------------

def calculation_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >=80:
        return "A"
    elif avg >=70:
        return "B"
    elif avg >= 60:
        return "c"
    else:
        return "F"
    
    def add_student():
        name = input ("Enter the student name")
        subjects = ["Maths","Science","English"]
        marks = {}

        for subject in subjects:
            score = int(input(f"Enter marks for {subject}:"))
            marks[subject] = score

            total = sum(marks.value())
            avg = total / len(subjects)
            grade =calculation_grade(avg)

            with open("report_card.txt","a") as f:
                f.write(f"{name} | Total: {total} | {avg:.2f}  | Grade: {grade}\n")

                print ("Report saved")

                def view_reports():
                    try:
                         with open("report_cards.txt", "r") as f:
                             print("\nSaved Report Cards:")
                             print(f.read())
                    except FileNotFoundError:
                          print("No reports found yet.")

            #main menue
            while True:
                print ("\n1. Add Report  2. View Reports  3. Exit")
                choice = input("choose an option: ")

                if choice == "1":
                    add_student()
                elif choice == "2":
                    view_reports()
                elif choice == "3":
                    print("Exiting.....")
                    break
                else:
                    print("invalid choice. Try again.")

                        



