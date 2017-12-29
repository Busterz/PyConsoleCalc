def add(*list_arg):
    # Getting the first argument: list_arg[0]
    if len(list_arg) == 1 and isinstance(list_arg[0], list):
        sum = 0
        # Iterate the list which is the first argument
        for n in list_arg[0]:
            sum += n
        return sum
    elif len(list_arg) > 1:
        print list_arg

def sub(*list_arg):
    if len(list_arg) == 1 and isinstance(list_arg[0], list):
        sum = list_arg[0].pop(0)
        for n in list_arg[0]:
            sum -= n
        return sum

def mult(*list_arg):
    if len(list_arg) == 1 and isinstance(list_arg[0], list):
        sum = 1
        for n in list_arg[0]:
            sum *= n
        return sum

def div(*list_arg):
    if len(list_arg) == 1 and isinstance(list_arg[0], list):
        sum = list_arg[0].pop(0)
        for n in list_arg[0]:
            sum /= n
        return sum

def mod(*list_arg):
    if len(list_arg) == 1 and isinstance(list_arg[0], list):
        sum = list_arg[0].pop(0)
        for n in list_arg[0]:
            sum %= n
        return sum

def power(*list_arg):
    if len(list_arg) == 1 and isinstance(list_arg[0], list):
        sum = list_arg[0].pop(0)
        base = sum
        print ("Your base is " + str(sum))
        for n in list_arg[0]:
            sum **= n
        return sum

def calc_logic_process(just_list, just_another_list, op_dict, index1, index2):
    temp_grouping = []
    temp_grouping.append(just_list[index1-1])
    temp_grouping.append(just_another_list[index2+1])
    res = op_dict[just_another_list[index2]](temp_grouping)
    return res

def calc_logic(any_list, op_dict):
    temp_result1 = []
    for n in range(len(any_list)):
        if any_list[n] in op_dict:
            if len(temp_result1) == 0:
                ans = calc_logic_process(any_list, any_list, op_dict, n, n)
                temp_result1.append(ans)
            else:
                ans = calc_logic_process(temp_result1, any_list, op_dict, len(temp_result1), n)
                temp_result1.append(ans)
    print ("The final result is " + str(temp_result1[len(temp_result1)-1]))

def replace_prec_grouping(temp_input_list, prec_index, l_index, temp_result):
    del temp_input_list[prec_index[l_index]+1]
    del temp_input_list[prec_index[l_index]]
    del temp_input_list[prec_index[l_index]-1]
    temp_input_list.insert(prec_index[l_index]-1, temp_result[len(temp_result)-1])

def operations(input_list):
    op_dict = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div,
        "%": mod,
        "**": power
    }
    prec = ['*', '/', '%', '**']
    prec_index = []
    temp_input_list = input_list

    if len(input_list) % 2 == 1:
        sum = 0
        for n in range(len(input_list)):
            if input_list[n] in prec:
                prec_index.append(n)
        if len(prec_index) > 0:
            restart = True;
            temp_result = []
            while restart:
                restart = False
                for l in range(len(prec_index)):
                    temp_grouping = []
                    temp_grouping.append(temp_input_list[prec_index[l]-1])
                    temp_grouping.append(temp_input_list[prec_index[l]+1])
                    res = op_dict[input_list[prec_index[l]]](temp_grouping)
                    temp_result.append(res)
                    # this is the part where in the original input, the segment with prec opt is replaced with the calculated result above
                    if len(prec_index) > 1:
                        # while counter != len(prec_index):
                        # replace the grouping with the calculated result above
                        # reset the len of prec_index by refinding the position of the rest of prec_operators
                        # calculate again
                        replace_prec_grouping(temp_input_list, prec_index, l, temp_result)

                        del prec_index[:] # same as del prec_index[0:len(prec_index)]
                        for n in range(len(temp_input_list)):
                            if input_list[n] in prec:
                                prec_index.append(n)
                        restart = True
                        break
                    elif len(prec_index) == 1:
                        replace_prec_grouping(temp_input_list, prec_index, l, temp_result)
            # this method is where calculation is done in groupings. Whenever there is math operator, the number before and number after the opt is calculated
            # only for plus minus only
            calc_logic(temp_input_list, op_dict)
        else:
            calc_logic(input_list, op_dict)
