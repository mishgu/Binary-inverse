def binary_inverse (list_bits):
    decimal_value = 0
    i = 0
    # loop for bit to number
    for el in list_bits:
        decimal_value += el*(-2)**i
        i+=1
    # if number is not 0
    if decimal_value != 0:
        i = 0
        # star process: mult bits by -1 
        result_list = [list_bits[0]]
        for el in list_bits[1:]:
            result_list.append(list_bits[i]+list_bits[i+1])
            i+=1
        result_list.append(list_bits[i])
        # end process !
        # when we mult we get 2 but bits is 0 or 1
        # then we delete 2
        result_list = result_list[::-1] # get reverse because we need go back to front
        i = 0
        for el in result_list:
            if (el == 2):
            	# case when 12* we change 00*
                if( result_list[i-1] == 1 and (result_list[i+1] == 1 or result_list[i+1] == 2)):
                    result_list[i-1] = 0
                    result_list[i] = 0
                # case when *021 we change 1101
                elif( result_list[i-1] == 0 and result_list[i+1] == 1):
                    #case when * == 1 then we get 2 but bits is 0 or 1
                    if (result_list[i-2] == 1):
                    	result_list[i-2] = 2
                    	result_list[i-1] = 1
                        result_list[i] = 0
                    	i-=2
                    	continue
                    #case when * == 0 
                    else:
                        result_list[i-2] = 1
                        result_list[i-1] = 1
                        result_list[i] = 0
                #case when 022 we change 010
                elif( result_list[i-1] == 0 and result_list[i+1] == 2):
                    result_list[i-1] = 0
                    result_list[i] = 1
                    result_list[i+1] = 0
            i+=1    
        result_list = result_list[::-1] #get normal list
        print " Input data\t{0}\n Desimal value\t{1}\n Invale value\t{2}\n Output date\t{3}\n".format(list_bits, decimal_value, decimal_value*(-1),result_list)
        return result_list
                
#test1
binary_inverse([1, 0, 0, 1])
#test2
binary_inverse([0,1,0,0,1])
#test3
binary_inverse([0, 1, 1, 0, 1, 1])
#test4
binary_inverse([1, 1, 0, 1, 1])
#test5
binary_inverse([1, 1, 1, 0, 0, 1, 1])
#test6
binary_inverse([1, 0, 1, 1, 0, 1])
#test7
binary_inverse([1,1, 1,1])
#test8
binary_inverse([1,1, 1,1,1,1,1])
#test9
binary_inverse([1,0, 1,1,1,0,1])

