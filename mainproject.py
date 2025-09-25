import time

# Admin login credentials
admin_credentials = {"keerthana": "keerthi123"}

# Question database with 4 default Python questions
questions_db = {
    "Python": [
        {
            "question":"[python]" "What will be value of the following python expression print(4+3%5)?",
            "options": ["7", "2", "4", "1"],
            "answer": 1
        },
        {
            "question": "[python]""Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": 3
        },
        {
            "question": "[python]""What data type is the result of: 3 / 2 in Python 3?",
            "options": ["int", "float", "double", "decimal"],
            "answer": 2
        },
        {
            "question":"[python]" "What does len('Hello') return?",
            "options": ["4", "5", "6", "Error"],
            "answer": 2
        }
    ],
    'MySQL':[
        {
            "question":"[MYsql]" "Which SQL statement is used to retrieve data from a mysql database?",
            "option":["UPDATE","INSERT","SELECT","DELETE"],
            "answer":3
        },
        {
            "question":"[MYsql]""what does SQL stand for.",
            "option":["structured question language","standard query logic","structured query language","simple query language"],
            "answer":3
        }
    ],
}
#list to store user quiz records
user_scores=[]
    #--------------admin login-------------------
def admin_login():
        print('\n--Admin Login--')
        username=input('username:')
        password=input('password:')
        if admin_credentials.get(username)==password:
            print('login successfully.\n')
        else:
            print('invalid credencials.\n')
    



def add_question():
    tech = input("Enter Technology (Python/MySQL): ").strip().capitalize()
    if tech not in questions_db:
        print("Invalid Technology.\n")
        return
    question = input("Enter question: ")
    options = [input(f"Option {i+1}: ") for i in range(4)]
    correct = int(input("Enter correct option (1-4): "))
    questions_db[tech].append({
        "question": question,
        "options": options,
        "answer": correct
    })
    print("Question added successfully.\n")

def modify_question():
    tech = input("Enter Technology (Python/MySQL): ").strip().capitalize()
    if tech not in questions_db or not questions_db[tech]:
        print("No questions found.\n")
        return
    view_all_questions(tech)
    q_num = int(input("Enter question number to modify: ")) - 1
    if 0 <= q_num < len(questions_db[tech]):
        question = input("Enter new question: ")
        options = [input(f"New Option {i+1}: ") for i in range(4)]
        correct = int(input("Enter new correct option (1-4): "))
        questions_db[tech][q_num] = {
            "question": question,
            "options": options,
            "answer": correct
        }
        print("Question updated successfully.\n")
    else:
        print("Invalid question number.\n")

def delete_question():
    tech = input("Enter Technology (Python/MySQL): ").strip().capitalize()
    if tech not in questions_db or not questions_db[tech]:
        print("No questions found.\n")
        return
    view_all_questions(tech)
    q_num = int(input("Enter question number to delete: ")) - 1
    if 0 <= q_num < len(questions_db[tech]):
        questions_db[tech].pop(q_num)
        print("Question deleted.\n")
    else:
        print("Invalid question number.\n")

def view_all_questions(tech=None):
    if tech is None:
        tech = input("Enter Technology (Python/MySQL): ").strip().capitalize()
    if tech not in questions_db or not questions_db[tech]:
        print("No questions to display.\n")
        return
    for idx, q in enumerate(questions_db[tech], start=1):
        print(f"{idx}. {q['question']}")
        for i, opt in enumerate(q['options'], start=1):
            print(f"   {i}. {opt}")
    print()

def view_all_users():
    if not user_scores:
        print("No user data available.\n")
        return
    for user in user_scores:
        print(f"{user['name']} | Mobile: {user['mobile']} | Score: {user['score']} | Time: {user['time']}")
    print()

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Question")
        print("2. Modify Question")
        print("3. Delete Question")
        print("4. View All Questions")
        print("5. View All Users")
        print("6. Logout")
        choice = input("Choice: ")
        if choice == '1':
            add_question()
        elif choice == '2':
            modify_question()
        elif choice == '3':
            delete_question()
        elif choice == '4':
            view_all_questions()
        elif choice == '5':
            view_all_users()
        elif choice == '6':
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")

# ---------------- User Functions ----------------

def user_login():
    print("\n---- User Login ----")
    name = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")
    print(f"Welcome, {name}!\n")
    user_menu(name, mobile)

def take_quiz(name, mobile):
    tech = input("Choose Technology (Python/MySQL): ").strip().capitalize()
    if tech not in questions_db or not questions_db[tech]:
        print("No quiz available for this technology.\n")
        return
    score = 0
    for q in questions_db[tech]:
        print(f"\n{q['question']}")
        for i, opt in enumerate(q['options'], start=1):
            print(f"{i}. {opt}")
        try:
            answer = int(input("Your answer (1-4): "))
            if answer == q['answer']:
                score += 1
        except:
            print("Invalid input. Skipping question.")
    total = len(questions_db[tech])
    print(f"\nQuiz Completed! Your Score: {score}/{total}")
    user_scores.append({
        "name": name,
        "mobile": mobile,
        "score": score,
        "time": time.strftime('%Y-%m-%d %H:%M:%S')
    })

def highest_scores():
    if not user_scores:
        print("No scores available.\n")
        return
    sorted_scores = sorted(user_scores, key=lambda x: x['score'], reverse=True)
    print("\n--- Top Scores ---")
    for user in sorted_scores[:3]:
        print(f"{user['name']} - {user['score']}")

def user_menu(name, mobile):
    while True:
        print("\n--- User Menu ---")
        print("1. Take Quiz")
        print("2. View Highest Scores")
        print("3. Logout")
        choice = input("Choice: ")
        if choice == '1':
            take_quiz(name, mobile)
        elif choice == '2':
            highest_scores()
        elif choice == '3':
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice.\n")

# ---------------- Main Menu ----------------

def main():
    while True:
        print("==== QUIZ SYSTEM ====")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            admin_login()
        elif choice == '2':
            user_login()
        elif choice == '3':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":

 main()
