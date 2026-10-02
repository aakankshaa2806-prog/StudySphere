print("="*45)
print("           WELCOME TO STUDYSPHERE")
print("="*45)

users = {}
tasks = []
notes = []
habits = []
study_plan = []
attendance = {}
cgpa_data = []

logged_in = False
current_user = ""

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    start_choice = input("Enter Choice: ")

    if start_choice == "1":

        print("\n========== REGISTRATION ==========")

        name = input("Name: ")
        age = int(input("Age: "))
        college = input("College: ")
        username = input("Create Username: ")
        password = input("Create Password: ")

        if username in users:
            print("Username already exists!")

        else:
            users[username] = {
                "name": name,
                "age": age,
                "college": college,
                "password": password
            }

            print("Registration Successful!")

    elif start_choice == "2":

        print("\n============== LOGIN ==============")

        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:

            logged_in = True
            current_user = username

            print("\nLogin Successful!")
            print(f"Welcome {users[username]['name']}!")

            while logged_in:

                print("\n")
                print("="*40)
                print("             DASHBOARD")
                print("="*40)

                print("1. Attendance Tracker")
                print("2. To-Do List")
                print("3. Notes")
                print("4. CGPA Calculator")
                print("5. Habit Tracker")
                print("6. Study Planner")
                print("7. Profile")
                print("8. Progress")
                print("9. Logout")

                choice = input("Enter Choice: ")

                if choice == "1":

                    while True:

                        print("\n")
                        print("="*40)
                        print("          ATTENDANCE TRACKER")
                        print("="*40)

                        print("1. Add Attendance")
                        print("2. View Attendance")
                        print("3. Classes Needed for 75%")
                        print("4. Back to Dashboard")

                        attendance_choice = input("Enter Choice: ")

                        if attendance_choice == "1":

                            subject = input("Enter Subject: ")
                            total = int(input("Total Classes: "))
                            attended = int(input("Classes Attended: "))

                            if attended > total:
                                print("Attended classes cannot be greater than total classes!")

                            else:
                                attendance[subject] = {
                                    "total": total,
                                    "attended": attended
                                }

                                percentage = (attended / total) * 100

                                print(f"Attendance: {percentage:.2f}%")

                                if percentage >= 75:
                                    print("Safe Attendance!")

                                else:
                                    print("Warning! Attendance is below 75%.")

                        elif attendance_choice == "2":

                            if len(attendance) == 0:
                                print("No attendance records available.")

                            else:
                                print("\n========== ATTENDANCE ==========")

                                for subject in attendance:

                                    total = attendance[subject]["total"]
                                    attended = attendance[subject]["attended"]

                                    percentage = (attended / total) * 100

                                    print(f"\nSubject: {subject}")
                                    print(f"Total Classes: {total}")
                                    print(f"Attended: {attended}")
                                    print(f"Attendance: {percentage:.2f}%")

                        elif attendance_choice == "3":

                            subject = input("Enter Subject: ")

                            if subject in attendance:

                                total = attendance[subject]["total"]
                                attended = attendance[subject]["attended"]

                                percentage = (attended / total) * 100

                                if percentage >= 75:
                                    print("You already have 75% or more attendance.")

                                else:
                                    required = 0

                                    while ((attended + required) / (total + required)) * 100 < 75:
                                        required += 1

                                    print(f"You need to attend {required} more classes to reach 75%.")

                            else:
                                print("Subject not found.")

                        elif attendance_choice == "4":
                            break

                        else:
                            print("Invalid Choice!")

                elif choice == "2":

                    while True:

                        print("\n")
                        print("="*40)
                        print("             TO-DO LIST")
                        print("="*40)

                        print("1. Add Task")
                        print("2. View Tasks")
                        print("3. Mark Task Complete")
                        print("4. Delete Task")
                        print("5. Back to Dashboard")

                        task_choice = input("Enter Choice: ")

                        if task_choice == "1":

                            task = input("Enter Task: ")

                            tasks.append({
                                "task": task,
                                "completed": False
                            })

                            print("Task Added Successfully!")

                        elif task_choice == "2":

                            if len(tasks) == 0:
                                print("No Tasks Available.")

                            else:

                                print("\n========== YOUR TASKS ==========")

                                for i in range(len(tasks)):

                                    if tasks[i]["completed"]:
                                        status = "Completed"
                                    else:
                                        status = "Pending"

                                    print(f"{i+1}. {tasks[i]['task']} - {status}")

                        elif task_choice == "3":

                            if len(tasks) == 0:
                                print("No Tasks Available.")

                            else:

                                for i in range(len(tasks)):
                                    print(f"{i+1}. {tasks[i]['task']}")

                                number = int(input("Enter Task Number: "))

                                if number >= 1 and number <= len(tasks):
                                    tasks[number-1]["completed"] = True
                                    print("Task Marked Complete!")

                                else:
                                    print("Invalid Task Number.")

                        elif task_choice == "4":

                            if len(tasks) == 0:
                                print("No Tasks Available.")

                            else:

                                for i in range(len(tasks)):
                                    print(f"{i+1}. {tasks[i]['task']}")

                                number = int(input("Enter Task Number: "))

                                if number >= 1 and number <= len(tasks):
                                    tasks.pop(number-1)
                                    print("Task Deleted!")

                                else:
                                    print("Invalid Task Number.")

                        elif task_choice == "5":
                            break

                        else:
                            print("Invalid Choice!")

                elif choice == "3":

                    while True:

                        print("\n")
                        print("="*40)
                        print("               NOTES")
                        print("="*40)

                        print("1. Add Note")
                        print("2. View Notes")
                        print("3. Search Note")
                        print("4. Delete Note")
                        print("5. Back to Dashboard")

                        note_choice = input("Enter Choice: ")

                        if note_choice == "1":

                            title = input("Enter Note Title: ")
                            content = input("Enter Note: ")

                            notes.append({
                                "title": title,
                                "content": content
                            })

                            print("Note Added Successfully!")

                        elif note_choice == "2":

                            if len(notes) == 0:
                                print("No Notes Available.")

                            else:

                                for i in range(len(notes)):
                                    print("\nNote", i+1)
                                    print("Title:", notes[i]["title"])
                                    print("Content:", notes[i]["content"])

                        elif note_choice == "3":

                            search = input("Enter title to search: ").lower()

                            found = False

                            for note in notes:

                                if search in note["title"].lower():

                                    print("\nTitle:", note["title"])
                                    print("Content:", note["content"])

                                    found = True

                            if not found:
                                print("Note not found.")

                        elif note_choice == "4":

                            if len(notes) == 0:
                                print("No Notes Available.")

                            else:

                                for i in range(len(notes)):
                                    print(f"{i+1}. {notes[i]['title']}")

                                number = int(input("Enter Note Number: "))

                                if number >= 1 and number <= len(notes):
                                    notes.pop(number-1)
                                    print("Note Deleted!")

                                else:
                                    print("Invalid Note Number.")

                        elif note_choice == "5":
                            break

                        else:
                            print("Invalid Choice!")

                elif choice == "4":

                    print("\n")
                    print("="*40)
                    print("          CGPA CALCULATOR")
                    print("="*40)

                    subjects = int(input("Enter Number of Subjects: "))

                    total_points = 0
                    total_credits = 0

                    for i in range(subjects):

                        print("\nSubject", i+1)

                        subject = input("Subject Name: ")
                        credit = float(input("Credits: "))
                        grade = float(input("Grade Point: "))

                        total_points = total_points + (credit * grade)
                        total_credits = total_credits + credit

                        cgpa_data.append({
                            "subject": subject,
                            "credit": credit,
                            "grade": grade
                        })

                    if total_credits > 0:

                        cgpa = total_points / total_credits

                        print(f"\nYour GPA is: {cgpa:.2f}")

                    else:
                        print("Credits cannot be zero.")

                elif choice == "5":

                    while True:

                        print("\n")
                        print("="*40)
                        print("           HABIT TRACKER")
                        print("="*40)

                        print("1. Add Habit")
                        print("2. View Habits")
                        print("3. Mark Habit Complete")
                        print("4. Back to Dashboard")

                        habit_choice = input("Enter Choice: ")

                        if habit_choice == "1":

                            habit = input("Enter Habit: ")

                            habits.append({
                                "habit": habit,
                                "completed": False
                            })

                            print("Habit Added Successfully!")

                        elif habit_choice == "2":

                            if len(habits) == 0:
                                print("No Habits Available.")

                            else:

                                for i in range(len(habits)):

                                    if habits[i]["completed"]:
                                        status = "Completed"
                                    else:
                                        status = "Pending"

                                    print(f"{i+1}. {habits[i]['habit']} - {status}")

                        elif habit_choice == "3":

                            if len(habits) == 0:
                                print("No Habits Available.")

                            else:

                                for i in range(len(habits)):
                                    print(f"{i+1}. {habits[i]['habit']}")

                                number = int(input("Enter Habit Number: "))

                                if number >= 1 and number <= len(habits):
                                    habits[number-1]["completed"] = True
                                    print("Habit Completed!")

                                else:
                                    print("Invalid Habit Number.")

                        elif habit_choice == "4":
                            break

                        else:
                            print("Invalid Choice!")

                elif choice == "6":

                    while True:

                        print("\n")
                        print("="*40)
                        print("           STUDY PLANNER")
                        print("="*40)

                        print("1. Add Study Session")
                        print("2. View Study Plan")
                        print("3. Mark Session Complete")
                        print("4. Back to Dashboard")

                        plan_choice = input("Enter Choice: ")

                        if plan_choice == "1":

                            subject = input("Subject: ")
                            date = input("Date: ")
                            time = input("Time: ")
                            hours = float(input("Study Hours: "))

                            study_plan.append({
                                "subject": subject,
                                "date": date,
                                "time": time,
                                "hours": hours,
                                "completed": False
                            })

                            print("Study Session Added!")

                        elif plan_choice == "2":

                            if len(study_plan) == 0:
                                print("No Study Sessions Available.")

                            else:

                                for i in range(len(study_plan)):

                                    status = "Completed" if study_plan[i]["completed"] else "Pending"

                                    print("\nSession", i+1)
                                    print("Subject:", study_plan[i]["subject"])
                                    print("Date:", study_plan[i]["date"])
                                    print("Time:", study_plan[i]["time"])
                                    print("Hours:", study_plan[i]["hours"])
                                    print("Status:", status)

                        elif plan_choice == "3":

                            if len(study_plan) == 0:
                                print("No Study Sessions Available.")

                            else:

                                for i in range(len(study_plan)):
                                    print(f"{i+1}. {study_plan[i]['subject']} - {study_plan[i]['date']}")

                                number = int(input("Enter Session Number: "))

                                if number >= 1 and number <= len(study_plan):
                                    study_plan[number-1]["completed"] = True
                                    print("Study Session Completed!")

                                else:
                                    print("Invalid Session Number.")

                        elif plan_choice == "4":
                            break

                        else:
                            print("Invalid Choice!")

                elif choice == "7":

                    while True:

                        print("\n")
                        print("="*40)
                        print("              PROFILE")
                        print("="*40)

                        print("Name:", users[current_user]["name"])
                        print("Age:", users[current_user]["age"])
                        print("College:", users[current_user]["college"])
                        print("Username:", current_user)

                        print("\n1. Edit Name")
                        print("2. Edit College")
                        print("3. Change Password")
                        print("4. Back to Dashboard")

                        profile_choice = input("Enter Choice: ")

                        if profile_choice == "1":

                            new_name = input("Enter New Name: ")
                            users[current_user]["name"] = new_name
                            print("Name Updated!")

                        elif profile_choice == "2":

                            new_college = input("Enter New College: ")
                            users[current_user]["college"] = new_college
                            print("College Updated!")

                        elif profile_choice == "3":

                            old_password = input("Enter Old Password: ")

                            if old_password == users[current_user]["password"]:

                                new_password = input("Enter New Password: ")
                                users[current_user]["password"] = new_password

                                print("Password Changed!")

                            else:
                                print("Wrong Password.")

                        elif profile_choice == "4":
                            break

                        else:
                            print("Invalid Choice!")

                elif choice == "8":

                    print("\n")
                    print("="*40)
                    print("           YOUR PROGRESS")
                    print("="*40)

                    completed_tasks = 0

                    for task in tasks:
                        if task["completed"]:
                            completed_tasks += 1

                    completed_habits = 0

                    for habit in habits:
                        if habit["completed"]:
                            completed_habits += 1

                    completed_sessions = 0
                    total_study_hours = 0

                    for session in study_plan:

                        total_study_hours += session["hours"]

                        if session["completed"]:
                            completed_sessions += 1

                    print("Total Tasks:", len(tasks))
                    print("Completed Tasks:", completed_tasks)

                    print("Total Habits:", len(habits))
                    print("Completed Habits:", completed_habits)

                    print("Study Sessions:", len(study_plan))
                    print("Completed Sessions:", completed_sessions)

                    print("Total Planned Study Hours:", total_study_hours)

                    if len(tasks) > 0:
                        task_percentage = (completed_tasks / len(tasks)) * 100
                        print(f"Task Completion: {task_percentage:.2f}%")

                    if len(habits) > 0:
                        habit_percentage = (completed_habits / len(habits)) * 100
                        print(f"Habit Completion: {habit_percentage:.2f}%")

                elif choice == "9":

                    print("Logging out...")
                    logged_in = False

                else:

                    print("Invalid Choice!")

        else:

            print("Invalid Username or Password.")

    elif start_choice == "3":

        print("Thank you for using StudySphere!")
        break

    else:

        print("Invalid Choice!")