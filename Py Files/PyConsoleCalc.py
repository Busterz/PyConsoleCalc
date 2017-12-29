from sys import exit
from CalcOperation import *
from CalcConversion import *

prompt = "> "

def calculate(op_choice):
    operationDict = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Division",
        5: "Modulo",
        6: "Power",
        7: "End"
    }
    print ("You picked %s.") % operationDict[op_choice]
    print ("What are your numbers? (Type '=' to start calculating)")
    num_list = []
    while True:
        num_input = raw_input(prompt)
        if num_input.lower() == "=":
            break
        else:
            num_list.append(float(num_input))
    return num_list

def chosen_op(choice):
    if choice == 1:
        list_args = calculate(choice)
        if len(list_args) > 0:
             res = add(list_args)
             print ("Result: " + str(res))
    elif choice == 2:
        list_args = calculate(choice)
        if len(list_args) > 0:
            res = sub(list_args)
            print ("Result: " + str(res))
    elif choice == 3:
        list_args = calculate(choice)
        if len(list_args) > 0:
            res = mult(list_args)
            print ("Result: " + str(res))
    elif choice == 4:
        list_args = calculate(choice)
        if len(list_args) > 0:
            res = div(list_args)
            print ("Result: " + str(res))
    elif choice == 5:
        list_args = calculate(choice)
        if len(list_args) > 0:
            res = mod(list_args)
            print ("Result: " + str(res))
    elif choice == 6:
        list_args = calculate(choice)
        if len(list_args) > 0:
            res = power(list_args)
            print ("Result: " + str(res))
    elif choice == 7:
        calc_cat()
    elif choice == 8:
        exit(0)

def print_ops():
    while True:
        print ("Please pick your operation: ")
        print ("1. Addition")
        print ("2. Subtraction")
        print ("3. Multiplication")
        print ("4. Division")
        print ("5. Modulo")
        print ("6. Power")
        print ("7. Back")
        print ("8. Quit")

        op_choice = int(raw_input(prompt))
        chosen_op(op_choice)

def print_diff_ops():
    num_op_list = []
    while True:
        print ("Input your number:")
        num_input = float(raw_input(prompt))
        num_op_list.append(num_input)
        print ("Input your operator: ('=' is an operator)")
        op_input = str(raw_input(prompt))
        if op_input == "=":
            operations(num_op_list)
            calc_cat()
            #break
        else:
            num_op_list.append(op_input)

def invoke_conversion(user_choice):
    if user_choice == 1:
        arg_input = raw_input("Input your word(s): ")
        arg_ouput = conv_eng_bin(arg_input)
        return (arg_ouput)
    elif user_choice == 2:
        arg_input = raw_input("Input your binary string: ")
        byte_str_output = conv_bin_eng(arg_input)
        return (byte_str_output)
    elif user_choice == 3:
        arg_input = int(raw_input("Input your integer: "))
        bin_output = str(conv_dec_bin(arg_input))
        return (bin_output)
    elif user_choice == 4:
        arg_input = raw_input("Input your binary: ")
        dec_output = str(conv_bin_dec(arg_input))
        return (dec_output)
    elif user_choice == 5:
        calc_cat()
    elif user_choice == 6:
        exit(0)

def invoke_conversion_convo():
    print ("1. Convert English to Binary")
    print ("2. Convert Binary to English")
    print ("3. Convert Integer to Binary")
    print ("4. Convert Binary to Integer")
    print ("5. Back")
    print ("6. Quit")
    user_choice = int(raw_input("Input your selection here: "))
    res = invoke_conversion(user_choice)
    print (res + "\n")
    invoke_conversion_convo()

def calc_cat():
    while True:
        print ("Which kind of calculation do you want to do?")
        print ("1. Calculation with 1 operation")
        print ("2. Calculation with more than 1 operations")
        print ("3. Conversion")
        print ("4. Quit")

        op_choice = int(raw_input(prompt))
        if op_choice == 1:
            print_ops()
            break
        elif op_choice == 2:
            print_diff_ops()
            break
        elif op_choice == 3:
            invoke_conversion_convo()
            break
        elif op_choice == 4:
            exit(0)
        else:
            print ("Option does not exist, please try again.")

user = raw_input("Hi there! What's your name? ")
user = user[0].upper() + user[1:]

print ("Alright %s, why are you here for?") % user
print ("1. Calculation")
print ("2. Say Hi")
print ("3. Quit")

while True:
    user_input = int(raw_input(prompt))
    if user_input == 1:
        print ("You chose %s.") % "Calculation"
        calc_cat()
        break
    elif user_input == 2:
        print ("%s") % "Hi!"
    elif user_input == 3:
        exit(0)
