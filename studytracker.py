import time
from datetime import datetime, timedelta

# File to store study sessions
TXT_FILE = 'study_sessions.txt'
last_logged_time = datetime.now()

# Function to log a study session
def log_study_session(subject, duration_minutes):
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"{date_str}|{subject}|{duration_minutes}\n"
    
    with open(TXT_FILE, 'a') as file:
        file.write(entry)
    global last_logged_time
    last_logged_time = datetime.now()
    print(f"Logged: {duration_minutes} minutes of {subject} on {date_str}.")

# Function to view all study sessions
def view_study_sessions():
    try:
        with open(TXT_FILE, 'r') as file:
            print("\nStudy Sessions:")
            print(f"{'ID':<5} {'Date':<20} {'Subject':<20} {'Duration (minutes)':<20}")
            print("-" * 70)
            for idx, line in enumerate(file, start=1):
                # Split the line into parts and check if it's properly formatted
                parts = line.strip().split('|')
                if len(parts) == 3:
                    date, subject, duration = parts
                    print(f"{idx:<5} {date:<20} {subject:<20} {duration:<20}")
                else:
                    print(f"{idx:<5} ERROR: Invalid data format")
    except FileNotFoundError:
        print("No study sessions found. Start logging your sessions!")

# Function to generate a study summary report
def generate_report():
    try:
        subjects = {}
        with open(TXT_FILE, 'r') as file:
            for line in file:
                _, subject, duration = line.strip().split('|')
                duration = int(duration)
                subjects[subject] = subjects.get(subject, 0) + duration

        print("\nStudy Summary:")
        print(f"{'Subject':<20} {'Total Duration (minutes)':<20}")
        print("-" * 40)
        for subject, total_duration in subjects.items():
            print(f"{subject:<20} {total_duration:<20}")
    except FileNotFoundError:
        print("No data to generate a report. Please log study sessions first.")

# Function to delete all study session data
def delete_all_data():
    open(TXT_FILE, 'w').close()
    print("All study session data has been deleted.")

# Function to delete a specific study session
def delete_specific_session():
    try:
        with open(TXT_FILE, 'r') as file:
            lines = file.readlines()
        view_study_sessions()
        session_id = int(input("Enter the session ID to delete: ")) - 1
        if 0 <= session_id < len(lines):
            del lines[session_id]
            with open(TXT_FILE, 'w') as file:
                file.writelines(lines)
            print("Study session deleted successfully.")
        else:
            print("Invalid session ID.")
    except (FileNotFoundError, ValueError):
        print("No sessions found or invalid input.")

# Function to edit a study session
def edit_study_session():
    try:
        with open(TXT_FILE, 'r') as file:
            lines = file.readlines()
        view_study_sessions()
        session_id = int(input("Enter the session ID to edit: ")) - 1
        if 0 <= session_id < len(lines):
            new_subject = input("Enter the new subject: ")
            new_duration = int(input("Enter the new duration in minutes: "))
            date, _, _ = lines[session_id].strip().split('|')
            lines[session_id] = f"{date}|{new_subject}|{new_duration}\n"
            with open(TXT_FILE, 'w') as file:
                file.writelines(lines)
            print("Study session updated successfully.")
        else:
            print("Invalid session ID.")
    except (FileNotFoundError, ValueError):
        print("No sessions found or invalid input.")

# Function to track study habits
def track_study_habits():
    try:
        morning, afternoon, evening = 0, 0, 0
        with open(TXT_FILE, 'r') as file:
            for line in file:
                date, _, duration = line.strip().split('|')
                duration = int(duration)
                hour = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').hour
                if 6 <= hour < 12:
                    morning += duration
                elif 12 <= hour < 18:
                    afternoon += duration
                else:
                    evening += duration

        print("\nStudy Habits Summary:")
        print(f"Morning (6 AM - 12 PM): {morning} minutes")
        print(f"Afternoon (12 PM - 6 PM): {afternoon} minutes")
        print(f"Evening/Night (6 PM - 6 AM): {evening} minutes")
    except FileNotFoundError:
        print("No data to analyze study habits.")

# Function for focus mode timer
def focus_mode_timer():
    subject = input("Enter the subject for the focus session: ")
    try:
        duration = int(input("Enter the duration for the focus session in minutes: "))
        print(f"Focus mode activated for {duration} minutes. Start studying!")
        time.sleep(duration * 60)
        log_study_session(subject, duration)
        print("Focus session complete and logged successfully.")
    except ValueError:
        print("Invalid input. Duration must be a number.")

# Main loop to handle user input
def main():
    while True:
        print("\n1. Log Study Session")
        print("2. View Study Sessions")
        print("3. Generate Report")
        print("4. Delete All Data")
        print("5. Delete Specific Study Session")
        print("6. Edit a Study Session")
        print("7. Track Study Habits")
        print("8. Focus Mode Timer")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            subject = input("Enter the subject: ")
            try:
                duration = int(input("Enter the duration in minutes: "))
                log_study_session(subject, duration)
            except ValueError:
                print("Invalid input. Duration must be a number.")
        elif choice == '2':
            view_study_sessions()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            delete_all_data()
        elif choice == '5':
            delete_specific_session()
        elif choice == '6':
            edit_study_session()
        elif choice == '7':
            track_study_habits()
        elif choice == '8':
            focus_mode_timer()
        elif choice == '9':
            print("Exiting. Happy studying!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the study tracker
if __name__ == "__main__":
    main()
