def binary_inverse (list_bits):
    decimal_value = 0
    i = 0
    for el in list_bits:
        decimal_value += el*(-2)**i
        i+=1
    if decimal_value != 0:
        i = 0
        result_list = [list_bits[0]]
        
        for el in list_bits[1:]:
            result_list.append(list_bits[i]+list_bits[i+1])
            i+=1
        result_list.append(list_bits[i])
        result_list = result_list[::-1]
        i = 0
        while i  != len(result_list):
            if (result_list[i] == 2):
                if( result_list[i-1] == 1 and result_list[i+1] == 1):
                    result_list[i-1] = 0
                    result_list[i] = 0
                elif( result_list[i-1] == 1 and result_list[i+1] == 2):
                    result_list[i-1] = 0
                    result_list[i] = 0
                elif( result_list[i-1] == 0 and result_list[i+1] == 1):
                    if (result_list[i-2] == 1):
                    	result_list[i-2] = 2
                    	result_list[i-1] = 1
                        result_list[i] = 0
                    	i-=2
                    	continue
                    else:
                        result_list[i-2] = 1
                        result_list[i-1] = 1
                        result_list[i] = 0
                elif( result_list[i-1] == 0 and result_list[i+1] == 2):
                    result_list[i-1] = 0
                    result_list[i] = 1
                    result_list[i+1] = 0    
            i+=1
        result_list = result_list[::-1]
        print " Input data\t{0}\n Desimal value\t{1}\n Invale value\t{2}\n Output date\t{3}\n".format(list_bits, decimal_value, decimal_value*(-1),result_list)
        return result_list

