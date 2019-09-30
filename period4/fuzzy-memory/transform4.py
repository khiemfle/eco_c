from PIL import Image

import random
import sys
import numpy as np

def qq(x, y):
	print "With {} and {}: ".format(x, y)
	return (2 * x + 3 * y + 29) % 256

def transform(pixelinfo):
	pixelreverse = [pixelinfo[len(pixelinfo)-1-i] for i in range(len(pixelinfo))]
	print "Pixelreverse: {}".format(pixelreverse)
	out = [pixelinfo[i] for i in range(len(pixelinfo))]
	print "Out: {}".format(out)
	for i in range(len(pixelinfo)):
		# Process on pixelreverse!!
		out[0] = qq(pixelreverse[i], out[0])
		print "  Out[0]: {}".format(out[0])
		for j in range(1,len(pixelinfo)):
			out[j] = qq(out[j-1], out[j])
			print "  Out[{}]: {}".format(j, out[j])
	print "Final out: {}".format(out)
	return out

def rev_qq(x32, x33):
	# x33 = (2*x32 + 3*x23 + 29) % 256
	# x33 = 2*x32 + 3*x23 + 29
	# x23 = ((x33 - 2*x32 - 29) / 3) % 256
	ret1 = x33 - 2*x32 - 29
	while True:
		print "{}".format(ret1)
		if ret1 % 3 == 0:
			re1 = ret1 / 3
			break
		else:
			ret1 = ret1 + 256
	
	ret1 = ret1%256

	if ret1 < 0:
	    ret1 = 256 + ret1

	return ret1


# Reverse transform!?!?
# def reverse(out):
#   	x31 = out[0]
# 	x32 = out[1]
# 	x33 = out[2]

# 	while True:
# 		x23 = rev_qq(x33, x32)
# 		x22 = rev_qq(x32, x31)
# 		x13 = rev_qq(x23, x22)

# 		A = np.array([(2, 3, 0), (, 1, -1), (0, 0, 1)])
# 		b = np.array([x32, x22, x13])
# 		x = np.linalg.solve(A, b)
# 	pass

# image = Image.open(sys.argv[1])
# outfile1 = Image.new(image.mode, image.size)

# for x in range(0, image.size[0]):
# 	for y in range(0, image.size[1]):
# 		sourcepixel = list(image.getpixel((x, y)))
# 		# sourcepixel is RGB!!
# 		print sourcepixel
# 		tran = transform(sourcepixel)
# 		outfile1.putpixel((x, y), tuple(tran))
# 		break
# 	break

a = 237
b = 65
c = 208
d = 117
print qq(117, 237)
print rev_qq(190, 70)
print qq(186, 15)
print rev_qq(186, 190)
print rev_qq(206, c)

# outfile1.save('out1.bmp')