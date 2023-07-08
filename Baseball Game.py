import random

def getThreeNumbers(): #returns list of 3 integer numbers
    three_numbers = random.sample(range(10), 3)
    return three_numbers 

def getNumbersFromUser(): #returns string 3 numbers
    while True:
        print("Input 3-digit numbers")
        user_input = input() 
        if user_input.isdigit():
            if len(list(user_input)) == 3:
                user_input = list(user_input)
                if user_input[0] == user_input[1] or user_input[1] == user_input[2] or user_input[0] == user_input[2]: #checking repeating values
                    user_input = "".join(str(i) for i in user_input)
                    print(user_input + " is an invalid input. Try again.")
                    continue
                else:
                    user_input = "".join(str(i) for i in user_input) #changes input back to integers
                    return str(user_input)
            else:
                print(user_input + " is an invalid input. Try again.")
                continue             
        else:
            print(user_input + " is an invalid input. Try again.")
            continue     
 
def checkNumbers(inputNumbers): #check if numbers are same
    global userNumber
    userNumber = inputNumbers
    global random_list
    OutputList = [0, 0, 0] #[Strike, Ball, Out]
    user_list = list(inputNumbers)
    #check if starts with 0
    if len(user_list) == 2:
        user_list.insert(0, "0")

    for a in range(3):
        if random_list[a]==user_list[a]: #if same position and value
            OutputList[0]+=1
        elif user_list[a] in random_list: #if diff position but in list
            OutputList[1]+=1
        
    if OutputList[0]==0 and OutputList[1]==0: 
        OutputList[2]+=1
    return OutputList
    
#MAIN CODE

print("Baseball game starts!")
OutCount = 0
random_list = [str(i) for i in getThreeNumbers()]
Try = 0
userNumber = ''

while True:
    while Try < 5: #0,1,2,3,4
        Try += 1
        StrBalOut = checkNumbers(getNumbersFromUser()) 
        if StrBalOut[2] == 1:
            OutCount+=1 
            print("Out!")
            if OutCount == 3: #three outs
                print("You Lose! The number is {}.".format("".join(random_list)))
                quit()
        else:
            if StrBalOut[0] == 0:
                print("{}: {}B".format(userNumber,StrBalOut[1])) 
            elif StrBalOut[1] == 0:
                print("{}: {}S".format(userNumber,StrBalOut[0])) 
            else:
                print("{}: {}S {}B".format(userNumber,StrBalOut[0], StrBalOut[1]))

            if StrBalOut[0] == 3:
                print("You Win!")
                quit()
    print("You Lose! The number is {}.".format("".join(random_list)))
    break
