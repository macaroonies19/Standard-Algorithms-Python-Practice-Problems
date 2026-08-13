test1 = int(input("What is your 1st test score? "))
test2 = int(input("What is your 2nd test score? "))
test3 = int(input("What is your 3rd test score? "))
totalscore = test1 + test2 + test3

if totalscore/3 >= 50:
    print("Pass")
else:
    print("Fail")
print("Your average score is:")
print(totalscore/3)