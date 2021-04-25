# I ran this through using windows powershell and typing the filename into the cmd line to run
while True:
	year = input("Enter year: ")

	try:
		year = int(year)
	except:
		print("Please enter a number")
		continue
	else:
		break

if (year%4) == 0:
	if (year%100) == 0:
		if (year%400) == 0:
			print("Is Prime")
		else:
			print("Not Prime")
	else:
		print("Is Prime")
else:
	print("Not Prime")

# Sorry for this I don't know Python at all so this is my stop gap so
# the window stays open so I can see the results
holup = input("Hit enter to exit")