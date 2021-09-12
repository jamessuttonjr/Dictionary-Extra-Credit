coursenumbers = {"CS101":["3004", "Haynes", "8:00a.m."],
                 "CS102":["4501", "Alvarado", "9:00a.m."],
                 "CS103":["6755", "Rich", "10:00a.m."],
                 "NT110":["1244", "Burke", "11:00a.m"],
                 "CM241":["1411", "Lee", "1:00p.m."]} 

coursechoice = input("Please enter a coure number: ")

list_of_keys = list(coursenumbers)
for key in list_of_keys:
    if key == coursechoice:
        print("Room Number: ", coursenumbers[key][0])
        print("Instructor: ", coursenumbers[key][1])
        print("Meeting Time: ", coursenumbers[key][2])

