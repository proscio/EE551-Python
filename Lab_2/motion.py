# Patrick Roscio
# January 29th, 2024
# Lab_2 motion.py

time = 10
v0= 8.25
acceleration = 5.25
print ("Time = ",time)

velocity = v0 + (acceleration*time)
avg_velocity = v0 + (0.5*(acceleration*time))
displacement = (v0*time)+ (0.5*(acceleration*(time ** 2)))

print ("Velocity = ", velocity)
print ("Average Velocity = ", avg_velocity)
print ("Displacement = ", displacement)
