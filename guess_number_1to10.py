#importing time module for sleep function
import time

#creating a function that contains the puzzle
def puzzle_time():
    print('Think of a number: 1...to...10\n')
    time.sleep(2) #just delaying for better experience 
    numbers = [2,5,10] #list of numbers - part of puzzle instructions
    cmds = ['Now, Multiply by ', 'And, Add '] #list of string - part of puzzle instructions
    #creating the sequence of puzzle instructions 
    for number in numbers:
        for cmd in cmds:
            print(cmd + str(number) + '\n') #str() used in print as print() takes only string and nummber is integer here
            time.sleep(2)
    #print('Mul x 2, + 2, x 5, + 5, x 10, + 10')
    time.sleep(0.05)
    #while loop to listen to user input about completion 
    while(input("Type 'done' once you are done calculating\n").lower() == 'done'): #string converted to lower_case to verify against only 'done'
        print('Great, Time for me to find out what the number is!\n')
        time.sleep(0.05)
        #typecasting (converting the input into integer as default input() returns string)
        num = int(input('Tell me what your calculated answer is is?\n'))
        print('..................\nFirst, Let me verify your Math skill ;)')
        time.sleep(0.1)
        if verify_calc(num): #calling verify_calc function to verify the calculated value
            print('Perfect, your calculation is!\n.....................\n')
            time.sleep(0.1)
            print('Time for the result:\n\n.....................\n')
            time.sleep(1)
            #directly calling the result_puzzle function inside print to avoid extra steps and variables
            print('And, The number you had in mind is.....' + str(result_puzzle(num))+'\n\n.....................\n') 
            return
        else:
            print('Oops, your math is poor :( Time to learn some addition & multiplication')
            return
        
#function to verify user's calculation
def verify_calc(num):
    if num%100 == 60:
        return True     
    else:
        return False
#function to caclulate the guessed number from the calculation    
def result_puzzle(num):
    return(int(num/100)-1)

    
if __name__ == "__main__":
    puzzle_time() #calling the puzzle function
    print('Thank you for playing!')
