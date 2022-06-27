import random
import os
usr_response = 'y' 

op_array = []
while usr_response == 'y':
	routput = random.randint(1, 6)
	op_array.append(routput)
	if routput == 1:
		print("=========")
		print("         ")
		print("    0    ")
		print("         ")
		print("=========")

	if routput == 2:
		print("=========")
		print("    0    ")
		print("         ")
		print("    0    ")
		print("=========")

	if routput == 3:
		print("=========")
		print("  0      ")
		print("    0    ")
		print("      0  ")
		print("=========")

	if routput == 4:
		print("=========")
		print("  0   0  ")
		print("         ")
		print("  0   0  ")
		print("=========")


	if routput == 5:
		print("=========")
		print(" 0     0 ")
		print("    0    ")
		print(" 0     0 ")
		print("=========")

	if routput == 6:
		print("=========")
		print(" 0     0 ")
		print(" 0     0 ")
		print(" 0     0 ")
		print("=========")
	
	usr_response = input("Press Y to continue.\t")
	os.system("cls")

print(op_array)
