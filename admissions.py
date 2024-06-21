'''
Program:  admissions.py. 

Programmer: Devon Chavez

Date: 05/17/2024

Description:  The program compares two college applicants. The program should prompt for each student's GPA, SAT, and ACT exam scores and report which candidate is more qualified on the basis of these scores.

'''
#introduction
print("This program compares two applicants to determine which one seems like the stronger")
print("applicant. For each candidate I will need either SAT or ACT scores as well as a weighted GPA.")

#Get information from first applicant
print("Information for the first applicant: ")
exam_type1 = int(input("Do you have 1) SAT scores or 2) ACT scores? "))

#User input is 1st applicant is trying to calculate sat scores
if exam_type1 == 1:
    math_score1 = int(input("SAT math? "))
    verbal_score1 = int(input("SAT verbal? "))
    gpa1 = float(input("Overall GPA? "))
    max_gpa1 = float(input("Max GPA? "))

#calculations for 1st applicant sat scores
    sat_score1 = (2 * verbal_score1 + math_score1) / 24.0
    gpa_score1 = gpa1 / max_gpa1 * 100.0
    applicant_1_score = sat_score1 + gpa_score1

#User input if 1st applicant is trying to calculate act score
elif exam_type1 == 2:
    english_score1 = int(input("ACT English? "))
    a_math_score1 = int(input("ACT Math? "))
    reading_score1 = int(input("ACT Reading? "))
    science_score1 = int(input("ACT Science? "))
    gpa1 = float(input("Overall GPA? "))
    max_gpa1  = float(input("Overall GPA? "))

#calculations for 1st applicant act scores
    act_score1 = (2 * reading_score1 + english_score1 + a_math_score1 + science_score1) / 1.8
    gpa_score1 = gpa1 / max_gpa1 * 100.0
    applicant_1_score = act_score1 + gpa_score1

print("Information for the second applicant:")
exam_type2 = int(input("Do you have 1) SAT scores or 2) ACT scores? "))

#User input if 2nd applicant is trying to calculate sat scores
if exam_type2 == 1:
    math_score2 = int(input("SAT math? "))
    verbal_score2 = int(input("SAT verbal? "))
    gpa2 = float(input("Overall GPA? "))
    max_gpa2 = float(input("Max GPA? "))

    sat_score2 = (2 * verbal_score2 + math_score2) / 24.0
    gpa_score2 = gpa2 / max_gpa2 * 100.0
    applicant_2_score2 = sat_score2 + gpa_score2

#User input if 2nd applicant is trying to calculate act scores
elif exam_type2 == 2:
    english_score2 = int(input("ACT English? "))
    a_math_score2 = int(input("ACT Math? "))
    reading_score2 = int(input("ACT Reading? "))
    science_score2 = int(input("ACT Science? "))
    gpa2 = float(input("Overall GPA? "))
    max_gpa2  = float(input("Overall GPA? "))

#calculations for 2nd applicant act scores
    act_score2 = (2 * reading_score2 + english_score2 + a_math_score2 + science_score2) / 1.8
    gpa_score2 = gpa2 / max_gpa2 * 100.0
    applicant_2_score = act_score2 + gpa_score2

# Displaying the overall scores
print("First applicant overall score = ", applicant_1_score)
print("Second applicant overall score = ", applicant_2_score)

# Display the final report
if applicant_1_score > applicant_2_score:
    print("The first applicant seems to be better")
elif applicant_2_score > applicant_1_score:
    print("The second applicant seems to be better")
else:
    print("The two applicants seem to be equal")