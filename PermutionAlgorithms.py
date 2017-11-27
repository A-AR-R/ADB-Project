__author__ = 'Alipour'

def fisher_yates_shuffle(the_list,keys):
    list_range = range(0, len(the_list))

    for i in list_range:
    # for i in range(4):
    #     j = randint(list_range[i], list_range[-1])
    #     keys.append(j)
        j=keys[i]
        the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list

def sattoloCycle(items,key):
    i = len(items)
    l=list(items)
    for key in [3,2,0,1]:
        i = i - 1
        l[key],l[i] = l[i],l[key]
    return l
