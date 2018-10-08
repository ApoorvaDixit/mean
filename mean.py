def mean(num_list):
    try:
        return float(sum(num_list))/len(num_list)
    except ZeroDivisionError :
        return 0
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
	return NotImplemented
        # raise TypeError(detail.__str__() + "\n" +  msg)
