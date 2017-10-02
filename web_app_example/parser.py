def solve_exponential(string, start, end, e_position):
    try:
        value = int(string[start: e_position])
        exponent = int(string[e_position+1: end+1])

        return '{0:.10f}'.format((value * (10 ** exponent)))
    except ValueError:
        return None


def parse_exponential(s):
        number = "0123456789."

        e_position = s.find('e')
        e_left = -1
        e_right = len(s)
        for x in range(e_position-2,0,-1):

            if number.find(s[x]) == -1:
                e_left = x
                break
        temp = len(s)
        for x in range(e_position+1,len(s)):

            if number.find(s[x]) != -1:
                temp = x
                break
        for x in range(temp+1,len(s)):
            print(s[x],'y')
            if number.find(s[x]) == -1:
                e_right = x
                break
        value = solve_exponential(s,e_left+1, e_right-1, e_position )
        if value == None:
            return None
        string = s[0:e_left+1] + str(value) + s[e_right:]
        return string

def parse(s):
    if not type(s) is str:
        return None
    if len(s) < 1:
        return None
    if 'e' in s:
        s = parse_exponential(s)
        if s == None:
        	return None
    if '+' in s:
        s_list = s.split("+")
        n_list = [parse(s) for s in s_list]
        if None in n_list:
            return None
        return sum(n_list)
    if s[0] == '-':
        return(-parse(s[1:]))
    n = 0
    dec = False
    divisor = 1.0
    if s == '.':
        return None
    for c in s:
        if c == '.':
            if dec:
                return None
            dec = True
        elif not dec:
            if not ('0' <= c <= '9'):
                return None
            n = n * 10
            n = n + ord(c) - ord('0')
        else:
            divisor = divisor / 10.0
            v = ord(c) - ord('0')
            n = n + v * divisor
    return n
