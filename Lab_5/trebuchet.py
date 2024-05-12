#Patrick Roscio
#Lab_5: trebuchet.py
#Takes in any number of trials from the user and returns the top 3 largest distances of the trebuchet runs. 

longest_distances = [0,0,0]
longest_trial_number = [0,0,0]

run = "Y"
trial_num = 1
while run == "Y":
    run = input("Would you like to continue? \n Enter \"Y\" to continue or anything else to view results: ")
    if run == "Y":    
        distance = int(input("Please enter the distance as an intiger: "))
        if distance >= longest_distances[0]:
            longest_distances[0],longest_distances[1],longest_distances[2] = distance,longest_distances[0],longest_distances[1]
            longest_trial_number[0],longest_trial_number[1],longest_trial_number[2] = trial_num,longest_trial_number[0],longest_trial_number[1]
            trial_num += 1
        elif distance < longest_distances[0] and distance >= longest_distances[1]:
            longest_distances[1],longest_distances[2]= distance,longest_distances[1]
            longest_trial_number[1],longest_trial_number[2] =  trial_num,longest_trial_number[1]
            trial_num +=1
        elif distance < longest_distances[1] and distance >= longest_distances[2]:
            longest_distances [2] = distance
            longest_trial_number[2] = trial_num
        else:
            trial_num +=1
    else :
        print ("*****END OF TEST*****")        

print ("Trial:   Distace:")
print("(",format(longest_trial_number[0], '2d'), ",", format(longest_distances[0],'5d'),")")
print("(",format(longest_trial_number[1], '2d'), ",", format(longest_distances[1],'5d'),")")
print("(",format(longest_trial_number[2], '2d'), ",", format(longest_distances[2],'5d'),")")

exit()
