while(True):
	step_one = int(input("Choose a number between 2 and 10: "))
	#Number chosen correction
	if (step_one < 2 or step_one > 10):
		print("You didn't pick a number between 2 and 10!")
	elif (step_one >= 2 & step_one <= 10):
		break

step_two = (((step_one * 2) + 5) * 50)
step_three = step_two + int(input("Put in 1769 if you celebrated your birthday this year, otherwise type in 1768: "))
year = int(input("Please put in you year of birth: "))
results = step_three - year

print("The first number is the number you chose, and the other two numbers are your age!!")
print(results)
