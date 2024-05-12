# Patrick Roscio
# February 6th, 2024
# Lab_3 battreUp.py

import random

distance = random.randrange (451)

print("The batter hit the ball ", distance, "feet")

if distance >= 400: 
    print ("The ball flew", distance, "feet and the batter scored a home run! That's one point for our team!")
elif distance < 400 and distance >= 135:
    print ("The ball flew", distance, "feet and the batter made it to third base!")
elif distance < 135 and distance >= 10:
    print ("The ball flew", distance, "feet and the batter made it to second base!")
elif distance < 10 and distance >= 1:
    print ("The ball flew", distance, "feet because the batter bunted, and made it to first base!")
else: 
    print ("Strike!")