import subprocess

def show_menu():
    print("Please choose an option:")
    print("1. Attendance System")
    print("2. Video Summarizer")
    print("3. Exit")

def cam_attendance():
    subprocess.run(['python', 'cam-attendance.py'])

def vid_attendance():
    subprocess.run(['python', 'vid-attendance.py'])

def video_summarizer():
    subprocess.run(['python', 'app.py'])

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print("1. Attendance using Camera")
        print("2. Attendance using Video")
        print("3. Exit")
        
        while True:
            Achoice = input("Enter your choice (1/2/3): ")
            
            if Achoice == '1':
                cam_attendance()
            elif Achoice == '2':
                vid_attendance()
            elif Achoice == '3':
                print("Exiting attendance system.")
                break
            else:
                print("Invalid choice, please try again.")
    
    elif choice == '2':
        video_summarizer()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
