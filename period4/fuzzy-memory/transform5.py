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
	# print (x33 - 2*x32 - 29 + 256)
	# ret = ((x33 - 2*x32 - 29)/3) % 256
	ret = ((x33 - 2*x32 - 29) * 171) % 256
	if ret < 0:
		ret = 256 + ret
	return ret


# Reverse transform!?!?
def reverse(out):
  	x31 = out[0]
	x32 = out[1]
	x33 = out[2]

	while True:
		x23 = rev_qq(x32, x33)
		x22 = rev_qq(x31, x32)
		x13 = rev_qq(x22, x23)

		print "{} {} {}".format(x31, x22, x13)

		# 350889a+171b+682(343d+7453)=58482c
		A = np.array([(2, 3, 0, 0), (0, 2, 3, 0), (0, 0, 2, 3), (350889, 171, -58482, 682*343)])
		b = np.array([x31-29, x22-29, x13-29, 682*7453])
		x = np.linalg.solve(A, b)
		print x
		break

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

x31=186
x22=15
x13=28
# print qq(117, 237)
print rev_qq(190, 70)
# print qq(186, 15)
print rev_qq(186, 190)
print rev_qq(93, 65)

print "{} and {}, {}".format((2*a+3*b)%256, x31-29, x31-29 + 256)
print "{} and {}, {}".format((2*b+3*c)%256, x22-29, x22-29 + 256)
print "{} and {}, {}".format((2*c+3*d)%256, x13-29, x13-29 + 256)
print "{} and {}".format((350889*a+171*b+682*(343*d+7453))%256, 58482*c%256)
reverse([186, 190, 70])
# print rev_qq(206, c)

# outfile1.save('out1.bmp')