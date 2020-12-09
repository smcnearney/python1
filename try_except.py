count = 0
user_input = (input('How high should we count?'))

try: 
    MAX = int(user_input)
    while(count <= MAX):
        print(count)
        # The following line means, "add 1 to the value of count"
        # aka count = count +1
        count += 1
except ValueError:
    # The following line is the exception message
    print("Please run the program again, this time with a number!")