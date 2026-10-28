# Accept student details
name = input("Enter student name: ")
usn = input("Enter student USN: ")
total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

# Validate input
if total_classes <= 0:
    print("Invalid input! Total classes must be greater than zero.")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input! Check the number of classes attended.")
else:
    # Calculate attendance percentage
    attendance = (attended_classes / total_classes) * 100

    # Determine eligibility category
    if attendance >= 85:
        category = "Excellent Attendance"
        eligibility = "Eligible for examination"
    elif attendance >= 75:
        category = "Satisfactory Attendance"
        eligibility = "Eligible for examination"
    else:
        category = "Attendance Shortage"
        eligibility = "Not eligible for examination"

    # Calculate additional classes required
    if attendance < 75:
        required_classes = 0
        while ((attended_classes + required_classes) / (total_classes + required_classes)) * 100 < 75:
            required_classes += 1
    else:
        required_classes = 0

    # Display attendance report
    print("\n===== STUDENT ATTENDANCE REPORT =====")
    print("Student Name:", name)
    print("Student USN:", usn)
    print("Total Classes:", total_classes)
    print("Classes Attended:", attended_classes)
    print(f"Attendance Percentage: {round(attendance, 2)}%")
    print("Attendance Category:", category)
    print("Examination Status:", eligibility)
    print("Additional Classes Needed:", required_classes)
    print("=====================================")