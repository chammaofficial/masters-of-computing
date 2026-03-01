#
# which.py - asks questions to find your Python
#
print("\nFind the mystery Python!\n")
print("Enter Y/N to the following questions...")
male = input("Are you male? ")
if male == "Y":
    beard = input("Do you have a beard? ")
    if beard == "Y":
        mystery = "Terry Gilliam"
    else:
        alive = input("Are you still alive? ")
        if alive != "Y":
            dementia = input("Did you have dementia? ")
            if dementia == "Y":
                mystery = "Terry Jones"
            else:
                mystery = "Graham Chapman"
        else:
            mo = input("Do you have a moustache? ")
            traveller = input("Are you a traveller? ")
            if mo == "Y":
                mystery = "John Cleese"
            elif traveller == "Y":
                mystery = "Michael Palin"
            else:
                mystery = "Eric Idle"
else:
    print("Not *technically* a python, however...")
    mystery = "Carole Cleveland"
print("\nYour mystery Python is: ", mystery, "\n")
