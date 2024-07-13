lines = 1
cheers = 2

def cheerleader(l_count, c_count):
    for line in range(1, l_count + 1):
        for space in range(1, line):
            print("   ", end = '')
        for cheer in range(1, c_count):
            print("Go Team ", end = '')
        print("Go")

cheerleader(lines, cheers)