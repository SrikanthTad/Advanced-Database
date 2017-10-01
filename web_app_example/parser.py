from decimal import Decimal
import random
import calc

def parse(s):
    if not type(s) is str:
        return None
    if len(s) < 1:
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

#       if "e" in outro:
#          newoutro = float(outro)
#          nnewoutro = format(newoutro, '.2f')
#
#          return nnewoutro
#
#      else:
#          choice = input("do you want your answer in scientific notation? (y/n)")
#          if choice == 'y':
#              yesschoice = float(outro)
#              yeschoice = Decimal(yesschoice)
#              return format(yeschoice, '.2e')
#          else:
#              return outro
#
#  print(parser(intro))
#
# # Mode 1: normal
# # But it has those extra 0's.
# def format_e1(n):
#     return format(n,'e');
#
# # Mode 2: decimal limit
# # example: 2 digit
# def format_e2(n):
#     return format(n,'.2e');
#
# # Mode 3: remove all trailing zeros automatically.
# def format_e3(n):
#     a = '%e' % n
#     return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]
