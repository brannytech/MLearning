# program to invite friends to a wedding party
# declare empty list
invitees = []

print ("******Enter quit to end the program******")

# prompt user to enter their name and sort the names in the list

active = True
while active:
    name = input('Enter name: ')
    name = name.strip().lower()

# check if the name already exist and remove any white space

    if name not in invitees:
        name = name.strip().lower()
        invitees.append(name)
    else:
        print("**** The name " + name + " already exist !!! Enter a new name.")

# order the list permanently u and quit the loop

    invitees.sort(reverse=False)
    if name == "quit":
        invitees.remove("quit")
        active = False

# loop through the list and print out the invitation

        for invitee in invitees:
            print("Dear " + invitee.title() + ", you are invited to the wedding.")
        print("...........Expecting you all at the venue.....")
        print("........Cheers.....")
       
