def main():
    print("Hello, welcome to Sogwiz Gym")
    dayInput = input("To get started, what day of the week would you like to workout:\t")
    if(not checkIfDayIsValid(dayInput)):
        print("Exiting because you trippin, foo!")
        exit(1)
    
    #if we got to here, it means the user input is valid
    trainerNickName = "sogwiz"
    print("\n...\nYour workout buddy, Sargon " + trainerNickName + " is excited to see you on " + dayInput + "!\n")
    
    #this is to work with python dictionaries (or hashmaps)
    workouts = {
        1:{'type':'Full Body','searchkey':'21519'}, 
        2:{'type':'Full Booty','searchkey':'5085'},
        3:{'type':'Easy Cardio','searchkey':'53214'},
        4:{'type':'High Intensity Intervals','searchkey':'28224'},
        5:{'type':'Body pump','searchkey':'53263'},
        6:{'type':'Tabata','searchkey':'53684'}
    }
    printString = ""
    for i in range(1,len(workouts)+1):
        printString += str(i) + " : " + str(workouts[i]['type']) + "\n"
    workoutType = int(input("Using the number, what kind of workout would you like to do?\n" + printString))
    if workoutType in workouts:
        print("Here's your Assyrian motivation for the " + workouts[workoutType]['type'] + " workout: \n" + getUrl(workouts[workoutType]))
    else:
        print("Invalid workout number input. Try again. buhbye")
        exit(1)
    

#there's a much more efficient built in way of doing this, but this serves 2 purposes
#1. it has a for loop that tracks array indexes
#2. it is a function that you can call from your main program
def checkIfDayIsValid(inputString):
    daysOfWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for dayIndex in range( len(daysOfWeek) ):
        if inputString.lower() == daysOfWeek[dayIndex].lower():
            return True
    #we looped through the list of possible days, didn't find one that matched
    return False

def getUrl(workout):
    urlPrefix = "http://sargonsays.com/searchkey"
    return urlPrefix + "/" + workout['searchkey']


if __name__ == "__main__":
    main()
