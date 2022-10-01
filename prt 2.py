attendance = 90 # mendatory
assignment_submitted = 75 # mendatory
sports_player = True # not mendatory

print(f"attendence criteria met? : {attendance >= 75}")
print(f"assignment criteria met? : {assignment_submitted >= 70}")
print(f"sports criteria met? : {sports_player}")

if attendance >= 75 and assignment_submitted >= 70:
    if sports_player:
        print("The student can get grace marks = +10")
    else:
        print("The student is eligible to appear in final exam but not extra grace marks")
else:
    print("The student is not eligible")
