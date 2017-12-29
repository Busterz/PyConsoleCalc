def conv_bin_eng(arg_input):
    joined_str = ''.join(arg_input.split(' '))
    while(len(joined_str) % 8 != 0 or not(joined_str.isdigit())):
        print("Sorry, the binary string has to be in byte size and no spaces. Please try again..")
        arg_input = raw_input("Input your binary string here: ")
        joined_str = ''.join(arg_input.split(' '))
    if(len(joined_str) % 8 == 0 and joined_str.isdigit()):
        print ("Converting Binary to English...")
        byte_string = ''.join(chr(int(joined_str[i*8:i*8+8],2)) for i in range(len(joined_str)//8))
        return (byte_string.decode())

def conv_eng_bin(arg_input):
    print ("Converting English to Binary...")
    arg_output = ' '.join(format(x, 'b').zfill(8) for x in bytearray(arg_input))
    return arg_output

def conv_dec_bin(arg_input):
    print ("Converting Decimal to Binary...")
    arg_output = "{0:b}".format(arg_input)
    return arg_output

def conv_bin_dec(arg_input):
    print ("Converting Binary to Decimal...")
    arg_output = int(arg_input, 2)
    return arg_output
