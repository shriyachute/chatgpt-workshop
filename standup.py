from datetime import datetime, timedelta
import time

# Configuration
meeting_time = "14:02"  # 10 AM every day
team_members = ["Alice", "Bob", "Charlie"]  # Team member names

# Function to print reminder
def print_reminder(member):
    print(f"Reminder: Stand-up meeting starts at {meeting_time}. Reminder sent to {member}.")

# Function to schedule stand-up
def schedule_standup():
    while True:
        current_time = datetime.now()
        scheduled_time = datetime.strptime(meeting_time, "%H:%M").replace(year=current_time.year, month=current_time.month, day=current_time.day)
        if current_time < scheduled_time:
            wait_time = (scheduled_time - current_time).total_seconds()
            time.sleep(wait_time)
            for member in team_members:
                print_reminder(member)
        time.sleep(60)  # Check every minute

# Main
if __name__ == "__main__":
    schedule_standup()
