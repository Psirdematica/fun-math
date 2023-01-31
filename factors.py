
def fact_num(num):
    pairs_list=[]
    sorted_set_list=[]
    for i in range(1,num+1):
        if (num%i)==0:
            i_pair=int(num/i)
            pairs_list_cont=[i,i_pair]
            pairs_list.append(pairs_list_cont)

    for j in pairs_list:
        for y in j:
            if y in sorted_set_list:
                continue
            else:
                sorted_set_list.append(y)

    sorted_set=sorted(sorted_set_list)

    print(pairs_list)
    print(f"The factors of {num} = {sorted_set}")

fact_num(36)