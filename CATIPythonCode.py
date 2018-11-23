import random
import time

call = 0

print(time.time())
start = time.time() #Start timing of the page

while (int(time.time() - start) le 121):     		#Loop runs until 2 mins (Approx time for the ring)
    randome = random.randint(0,100)         		#This line is just for simulation
    call = randome                          		#This line is just for simulation
    print(call)                             			#This line is just for debugging
    if int(call) == 1:                      		#If call == 1, this means call is still ringing and waiting for the respondent.
        print(call, " Calling")             			#This line is just for debugging
        continue                            		#It will re-run the code again, until it fails the condition
    elif (call) == 2:                       		#If call == 2, this means that call is picked by the respondent.
        print(call, " Respondent picked the call") 	#This line is just for debugging
        break                               		#This will break the loop and move on.
