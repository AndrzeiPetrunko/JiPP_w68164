def inputValue(msg, start = 0, end = None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print("Wrong input arguments.")
        elif start is not None and end is not None:
            if not (start  <= int(inp) <= end):
                print("Wrong input arguments.")
            return int(inp)
        return int(inp)