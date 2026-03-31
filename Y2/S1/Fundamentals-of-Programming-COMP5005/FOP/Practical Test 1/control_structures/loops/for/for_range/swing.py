#Student Name: Konthasingha Waduge Chamod Priyamal Kumarasiri
#Student ID: 19739335
#swing.py: Prac test 1 - swinging boat ride


#Getting the user input for width and validate it.
width = int(input("Enter width of swing (5-10): "))
while width < 5 or width > 10 :
    print("Out of range, please re-enter...")
    width = int(input("Enter width of swing (5-10): "))


#Getting the user input for timesteps and validate it.
steps = int(input("Enter number of timesteps (10-50): "))
while steps < 10 or steps > 50 :
    print("Out of range, please re-enter...")
    steps = int(input("Enter number of timesteps (10-50): "))

boat_pos = 0
boat_dir = "R"


for t in range(steps):
    
    if boat_dir == "R":
        print(" " * boat_pos + "\###/")
        boat_pos = boat_pos + 1
        if boat_pos == width:
            boat_pos = boat_pos - 1
            boat_dir = "L"
    else:
        boat_pos = boat_pos - 1
        print(" " * boat_pos + "\###/")
        if boat_pos == 0:
            boat_dir = "R"
