import time

# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
CORRECT_MARKS  =  4
WRONG_MARKS    = -1
SKIP_MARKS     =  0
MIN_QUESTIONS  = 10

ADMIN_USERNAME = "ecat_admin"
ADMIN_PASSWORD = "ecat@2024"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "student123"

# ─────────────────────────────────────────────
#  DATA — QUESTION BANK
# ─────────────────────────────────────────────
questions = [
    {"id": 1,  "subject": "Physics",   "question": "What is the SI unit of force?",
     "choices": {"A": "Watt", "B": "Newton", "C": "Joule", "D": "Pascal"}, "answer": "B"},
    {"id": 2,  "subject": "Physics",   "question": "Speed of light in vacuum is approximately?",
     "choices": {"A": "3x10^6 m/s", "B": "3x10^8 m/s", "C": "3x10^10 m/s", "D": "3x10^4 m/s"}, "answer": "B"},
    {"id": 3,  "subject": "Chemistry", "question": "What is the atomic number of Carbon?",
     "choices": {"A": "4", "B": "8", "C": "6", "D": "12"}, "answer": "C"},
    {"id": 4,  "subject": "Chemistry", "question": "Which gas is most abundant in the atmosphere?",
     "choices": {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Hydrogen", "D": "Nitrogen"}, "answer": "D"},
    {"id": 5,  "subject": "Maths",     "question": "What is the value of sin(90°)?",
     "choices": {"A": "0", "B": "0.5", "C": "1", "D": "-1"}, "answer": "C"},
    {"id": 6,  "subject": "Maths",     "question": "Derivative of x² is?",
     "choices": {"A": "x", "B": "2x", "C": "x²", "D": "2"}, "answer": "B"},
    {"id": 7,  "subject": "English",   "question": "Choose the correct spelling:",
     "choices": {"A": "Accomodate", "B": "Acommodate", "C": "Accommodate", "D": "Acomodate"}, "answer": "C"},
    {"id": 8,  "subject": "English",   "question": "Antonym of 'Ancient' is?",
     "choices": {"A": "Old", "B": "Modern", "C": "Historic", "D": "Aged"}, "answer": "B"},
    {"id": 9,  "subject": "Physics",   "question": "Which law states F = ma?",
     "choices": {"A": "Newton's 1st Law", "B": "Newton's 3rd Law", "C": "Newton's 2nd Law", "D": "Hooke's Law"}, "answer": "C"},
    {"id": 10, "subject": "Chemistry", "question": "pH of pure water is?",
     "choices": {"A": "5", "B": "9", "C": "7", "D": "14"}, "answer": "C"},
    {"id": 11, "subject": "Maths",     "question": "What is log(100) base 10?",
     "choices": {"A": "1", "B": "3", "C": "10", "D": "2"}, "answer": "D"},
    {"id": 12, "subject": "English",   "question": "Synonym of 'Brave' is?",
     "choices": {"A": "Coward", "B": "Fearful", "C": "Courageous", "D": "Timid"}, "answer": "C"},
]

all_results = []  # stores every student result

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────
def separator():
    print("\n" + "=" * 50)

def pause():
    time.sleep(1)

def calculate_grade(percentage):
    if percentage >= 80:
        return "EXCELLENT"
    elif percentage >= 65:
        return "GOOD"
    elif percentage >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"

def calculate_score(answers_dict):
    correct = wrong = skipped = 0
    for idx, choice in answers_dict.items():
        if choice == "S":
            skipped += 1
        elif questions[idx]["answer"] == choice:
            correct += 1
        else:
            wrong += 1
    score = (correct * CORRECT_MARKS) + (wrong * WRONG_MARKS)
    max_score = len(questions) * CORRECT_MARKS
    percentage = round((score / max_score) * 100, 2) if max_score > 0 else 0
    return correct, wrong, skipped, score, max_score, percentage

# ─────────────────────────────────────────────
#  ADMIN FUNCTIONS
# ─────────────────────────────────────────────
def admin_login():
    separator()
    print("       ADMIN PORTAL — LOGIN")
    separator()
    attempts = 0
    while attempts < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\n  Login successful! Welcome, ECAT Team.")
            pause()
            return True
        else:
            attempts += 1
            print(f"  Try again. Attempts left: {3 - attempts}")
    print("\n  Account locked after 3 failed attempts.")
    return False

def view_all_questions():
    separator()
    print("         QUESTION BANK")
    separator()
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}. [{q['subject']}] {q['question']}")
        for key, val in q["choices"].items():
            print(f"     {key}) {val}")
        print(f"      Correct Answer: {q['answer']}")

def add_question():
    separator()
    print("         ADD NEW QUESTION")
    separator()
    subject  = input("Subject: ").strip()
    question = input("Question text: ").strip()
    print("Enter 4 choices:")
    a = input("A) ").strip()
    b = input("B) ").strip()
    c = input("C) ").strip()
    d = input("D) ").strip()
    while True:
        answer = input("Correct answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("Invalid! Enter A, B, C or D.")
    new_q = {
        "id": len(questions) + 1,
        "subject": subject,
        "question": question,
        "choices": {"A": a, "B": b, "C": c, "D": d},
        "answer": answer
    }
    questions.append(new_q)
    print(f"\n  Question added! Total questions: {len(questions)}")

def delete_question():
    separator()
    print("         DELETE QUESTION")
    separator()
    view_all_questions()
    try:
        num = int(input("\nEnter question number to delete: "))
        if 1 <= num <= len(questions):
            removed = questions.pop(num - 1)
            print(f"\n  Deleted: {removed['question']}")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Enter a valid number.")

def question_bank_stats():
    separator()
    print("       QUESTION BANK STATISTICS")
    separator()
    subjects = {}
    for q in questions:
        subjects[q["subject"]] = subjects.get(q["subject"], 0) + 1
    print(f"Total Questions: {len(questions)}\n")
    print("Breakdown by Subject:")
    for subj, count in subjects.items():
        print(f"  {subj}: {count} questions")

def view_all_student_results():
    separator()
    print("       ALL STUDENT RESULTS")
    separator()
    if not all_results:
        print("No student results yet.")
        return
    print(f"{'#':<4} {'Name':<20} {'Roll':<12} {'Score':<8} {'%':<8} {'Grade':<14} {'Time'}")
    print("-" * 75)
    for i, r in enumerate(all_results):
        print(f"{i+1:<4} {r['name']:<20} {r['roll']:<12} {r['score']:<8} {r['percentage']:<8} {r['grade']:<14} {r['time']}")

def view_detailed_result():
    separator()
    print("     DETAILED RESULT — PER STUDENT")
    separator()
    if not all_results:
        print("No student results yet.")
        return
    view_all_student_results()
    try:
        num = int(input("\nEnter result number to view: "))
        if 1 <= num <= len(all_results):
            r = all_results[num - 1]
            separator()
            print(f"Student: {r['name']}  |  Roll: {r['roll']}")
            print(f"Score: {r['score']}/{r['max_score']}  |  {r['percentage']}%  |  Grade: {r['grade']}")
            separator()
            for idx, choice in r["answers"].items():
                q = questions[idx] if idx < len(questions) else None
                if q:
                    status = "✔" if choice == q["answer"] else ("—" if choice == "S" else "✘")
                    print(f"\nQ{idx+1}. {q['question']}")
                    print(f"     Your Answer: {choice}  |  Correct: {q['answer']}  {status}")
        else:
            print("✘  Invalid number.")
    except ValueError:
        print("✘  Enter a valid number.")

def class_result_statistics():
    separator()
    print("       CLASS RESULT STATISTICS")
    separator()
    if not all_results:
        print("No student results yet.")
        return
    scores = [r["score"] for r in all_results]
    percentages = [r["percentage"] for r in all_results]
    grades = [r["grade"] for r in all_results]
    max_score = questions[0]["id"] if questions else 1
    pass_count  = sum(1 for p in percentages if p >= 50)
    fail_count  = len(all_results) - pass_count
    print(f"Total Students  : {len(all_results)}")
    print(f"Highest Score   : {max(scores)}")
    print(f"Lowest Score    : {min(scores)}")
    print(f"Average Score   : {round(sum(scores)/len(scores), 2)}")
    print(f"Pass            : {pass_count}")
    print(f"Fail            : {fail_count}")
    print("\nGrade Distribution:")
    for g in ["EXCELLENT", "GOOD", "AVERAGE", "BELOW AVERAGE"]:
        print(f"  {g}: {grades.count(g)}")

def admin_menu():
    if not admin_login():
        return
    while True:
        separator()
        print("         ADMIN PORTAL — MENU")
        separator()
        print(" 1. View All Questions")
        print(" 2. Add New Question")
        print(" 3. Delete Question")
        print(" 4. Question Bank Statistics")
        print(" 5. View All Student Results")
        print(" 6. View Detailed Result (Per Student)")
        print(" 7. Class Result Statistics")
        print(" 8. Logout")
        separator()
        choice = input("Select option (1-8): ").strip()
        if   choice == "1": view_all_questions()
        elif choice == "2": add_question()
        elif choice == "3": delete_question()
        elif choice == "4": question_bank_stats()
        elif choice == "5": view_all_student_results()
        elif choice == "6": view_detailed_result()
        elif choice == "7": class_result_statistics()
        elif choice == "8":
            print("\n✔  Logged out from Admin Portal.")
            break
        else:
            print("✘  Invalid option. Enter 1-8.")

# ─────────────────────────────────────────────
#  STUDENT FUNCTIONS
# ─────────────────────────────────────────────
def student_login():
    separator()
    print("       STUDENT PORTAL — LOGIN")
    separator()
    attempts = 0
    while attempts < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username == STUDENT_USERNAME and password == STUDENT_PASSWORD:
            print("\n✔  Login successful!")
            name = input("Enter your Full Name : ").strip()
            roll = input("Enter your Roll Number: ").strip()
            pause()
            return True, name, roll
        else:
            attempts += 1
            print(f"✘  Invalid credentials. Attempts left: {3 - attempts}")
    print("\n✘  Account locked after 3 failed attempts.")
    return False, "", ""

def view_exam_rules():
    separator()
    print("           EXAM RULES")
    separator()
    print(f"  • Total Questions : {len(questions)}")
    print(f"  • Correct Answer  : +{CORRECT_MARKS} marks")
    print(f"  • Wrong Answer    : {WRONG_MARKS} mark")
    print(f"  • Skipped         :  {SKIP_MARKS} marks")
    print("  • Type A/B/C/D    : to answer")
    print("  • Type S          : to skip")
    print("  • Type SUBMIT     : to end exam early")
    separator()

def start_exam(name, roll):
    separator()
    print(f"  Exam Started for: {name} | Roll: {roll}")
    print(f"  Total Questions : {len(questions)}")
    separator()
    answers_dict = {}
    for idx, q in enumerate(questions):
        print(f"\nQ{idx+1}/{len(questions)}. [{q['subject']}] {q['question']}")
        for key, val in q["choices"].items():
            print(f"     {key}) {val}")
        while True:
            ans = input("  Your Answer (A/B/C/D | S=Skip | SUBMIT=End): ").strip().upper()
            if ans == "SUBMIT":
                print("\n  Exam submitted early!")
                # fill remaining as skipped
                for remaining in range(idx, len(questions)):
                    if remaining not in answers_dict:
                        answers_dict[remaining] = "S"
                save_result(name, roll, answers_dict)
                return
            elif ans in ["A", "B", "C", "D", "S"]:
                answers_dict[idx] = ans
                break
            else:
                print("  ✘ Invalid input! Enter A, B, C, D, S or SUBMIT.")
    save_result(name, roll, answers_dict)

def save_result(name, roll, answers_dict):
    correct, wrong, skipped, score, max_score, percentage = calculate_score(answers_dict)
    grade = calculate_grade(percentage)
    exam_time = time.strftime("%d-%b-%Y %I:%M %p")
    result = {
        "name"      : name,
        "roll"      : roll,
        "correct"   : correct,
        "wrong"     : wrong,
        "skipped"   : skipped,
        "score"     : score,
        "max_score" : max_score,
        "percentage": percentage,
        "grade"     : grade,
        "time"      : exam_time,
        "answers"   : answers_dict
    }
    all_results.append(result)
    separator()
    print("           EXAM RESULT")
    separator()
    print(f"  Name       : {name}")
    print(f"  Roll No    : {roll}")
    print(f"  Correct    : {correct}  |  Wrong: {wrong}  |  Skipped: {skipped}")
    print(f"  Score      : {score} / {max_score}")
    print(f"  Percentage : {percentage}%")
    print(f"  Grade      : {grade}")
    separator()
    print("\n  Per-Question Review:")
    for idx, choice in answers_dict.items():
        if idx < len(questions):
            q = questions[idx]
            if choice == "S":
                status = "— SKIPPED"
            elif choice == q["answer"]:
                status = "✔ CORRECT"
            else:
                status = f"✘ WRONG (Correct: {q['answer']})"
            print(f"  Q{idx+1}. Your: {choice}  {status}")

def student_menu():
    success, name, roll = student_login()
    if not success:
        return
    while True:
        separator()
        print("       STUDENT PORTAL — MENU")
        separator()
        print(" 1. View Exam Rules")
        print(" 2. Start Exam")
        print(" 3. Logout")
        separator()
        choice = input("Select option (1-3): ").strip()
        if   choice == "1": view_exam_rules()
        elif choice == "2": start_exam(name, roll)
        elif choice == "3":
            print("\n✔  Logged out from Student Portal.")
            break
        else:
            print("✘  Invalid option. Enter 1-3.")

# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────
def main():
    while True:
        separator()
        print("     ECAT EXAM APPLICATION")
        print("     UET Lahore — CMPE-112L")
        separator()
        print(" 1. Admin Portal")
        print(" 2. Student Portal")
        print(" 3. Exit")
        separator()
        choice = input("Select portal (1-3): ").strip()
        if   choice == "1": admin_menu()
        elif choice == "2": student_menu()
        elif choice == "3":
            print("\n  Goodbye! — ECAT App Closed.\n")
            break
        else:
            print("✘  Invalid option. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()