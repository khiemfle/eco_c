from PIL import Image

import random
import sys

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

image = Image.open(sys.argv[1])
outfile1 = Image.new(image.mode, image.size)

for x in range(0, image.size[0]):
    for y in range(0, image.size[1]):
        sourcepixel = list(image.getpixel((x, y)))
        # sourcepixel is RGB!!
        print sourcepixel
        tran = transform(sourcepixel)
        outfile1.putpixel((x, y), tuple(tran))
        break
    break

outfile1.save('out1.bmp')