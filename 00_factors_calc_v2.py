# Functions go here
from email import header
from urllib import response

# Puts series of symbols at start and end of text
def statement_generator(text, decoration):

    # Make string with five characters 
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information [TO BE DONE LATER]
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Enter a interger that is between 1 and 200.")
    print()
    print("This program calculates the factors of this interger and then displays them on screen.")
    print("It will also display whether the interger is a prime number or a perfect square.")
    print()
    print("Complete as many calculaations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# checks input is a number more than given value
def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:
        print()
        error = "please enter an interger that is more than zero and 200 or under"

        try:
        
            low_num = 1
            high_num = 200
            
            # Ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero or under 200
            if low_num <= response <= high_num:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)


# Find square root of interger


# Gets factors, returns a sorted list
def get_factors(to_factor):

    # empty list to hold factors
    my_list = []

    # find factors...
    for item in range(1, to_factor + 1):
        if to_factor % item == 0:
            my_list.append(item)
            # my_list.append(to_factor)

    # sort the list
    my_list.sort()

    # my_list_len = len(my_list)

    # print the sorted list
    return(my_list)





# Main routine goes here


# Heading 
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue: ")
print()

if first_time == "":
    instructions()

    

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # Ask user for a number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"
        print()
    
    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)


    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special"

    else:
        heading = "Factors of {}".format(var_to_factor)
                
    # output factors and comment
    statement_generator(heading, "*")
    print(factor_list)
    print(comment)
    
    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()


