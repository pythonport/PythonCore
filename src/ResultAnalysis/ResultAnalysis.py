import re
import pandas as pd

# File path
file_path = "69543.TXT"

students = []

with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()

    # Match student main line (Roll No + Name + Result)
    match = re.match(r"(\d{8})\s+[MF]\s+([A-Z\s]+?)\s+.*\s+(PASS|ABST)", line)

    if match:
        roll = match.group(1)
        name = match.group(2).strip()
        result = match.group(3)

        # Next line contains marks
        marks_line = lines[i + 1].strip()
        marks_raw = marks_line.split()

        marks = []
        for m in marks_raw:
            if m == "AB":
                marks.append(0)
            else:
                try:
                    marks.append(int(m))
                except:
                    pass

        total = sum(marks)
        subjects = len(marks)
        percentage = round(total / subjects, 2) if subjects > 0 else 0

        students.append({
            "Roll": roll,
            "Name": name,
            "Result": result,
            "Marks": marks,
            "Total": total,
            "Percentage": percentage
        })

        i += 2  # Skip marks line
    else:
        i += 1

# Convert to DataFrame
df = pd.DataFrame(students)

# ---------------------------
# 📊 ANALYSIS
# ---------------------------

# Top 5 students
topper = df.sort_values(by="Percentage", ascending=False).head(5)

# Overall stats
total_students = len(df)
passed = len(df[df["Result"] == "PASS"])
absent = len(df[df["Result"] == "ABST"])
avg_percentage = df["Percentage"].mean()

# ---------------------------
# 📌 OUTPUT
# ---------------------------

print("\n===== TOP 5 STUDENTS =====")
print(topper[["Roll", "Name", "Percentage"]])

print("\n===== SUMMARY =====")
print(f"Total Students: {total_students}")
print(f"Passed: {passed}")
print(f"Absent: {absent}")
print(f"Pass Percentage: {round((passed/total_students)*100, 2)}%")
print(f"Average Percentage: {round(avg_percentage, 2)}%")

# Save to CSV
df.to_csv("cbse_result_analysis.csv", index=False)

print("\n✅ Report saved as 'cbse_result_analysis.csv'")