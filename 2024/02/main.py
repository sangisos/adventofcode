

def main():
	rawinput = None
	with open("input_test") as f:
		rawinput = f.readlines()
	if rawinput == None:
		return -1
	
	print(rawinput)

if __name__ == "__main__":
	main()
