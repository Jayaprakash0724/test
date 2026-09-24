# app.py
import sys

# Default values if no arguments are provided
course_name = "DevOps Engineering"
student_count = sys.argv[1] if len(sys.argv) > 1 else "45"

# Write the report
with open("build_report.txt", "w") as f:
    f.write(f"Course Name: {course_name}\n")
    f.write(f"Students Enrolled: {student_count}\n")

print(f"Report generated successfully with {student_count} students.")
