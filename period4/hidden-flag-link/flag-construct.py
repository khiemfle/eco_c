flag = "ttm4536{{{}}}"

c1 = chr(11 + 41)
c2 = "B"
c3 = "{0:{fill}13b}".format(2000, fill='0')

body = "{}{}{}".format(c1, c2, c3)

print flag.format(body)
# ttm4536{4B11111010000}
# ttm4536{4B0b11111010000}
# ttm4536{4B011111010000}
# ttm4536{4B00011111010000}
# ttm4536{4B0011111010000}
# ttm4536{4B0011111010000}