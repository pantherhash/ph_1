# https://raw.github.com/pantherhash/ph_1/master/ph_1.py
from PIL import Image
import urllib
import sys
from hashlib import sha1

# Approach 1: Run this program and print out the images.
# Approach 2: Don't run this program. The answer is in the code.

# celeb functions
def celeb_to_int(celeb):
	h = sha1()
	h.update(celeb)
	return int(h.hex_digest(), 16)

M = celeb_to_int("MT") # Mikkel Thorup
A = celeb_to_int("AH") # Anders Hejlsberg
P = celeb_to_int("PN") # Peter Naur
B = celeb_to_int("BS") # Bjarne Stoustrup

celebs_coords = [] # TODO

# constants

image_size = (2048, 2048)
base_urls = ['https://raw.github.com/pantherhash/ph_1/master/xkcd_images/',\
             'https://raw.github.com/pantherhash/ph_1/master/custom_images/']


start_node = (0, 0)

# state
explored = {}
stack = [start_node]

# functions
tr = lambda idx: (\
   abs(idx[1]) if idx[1] < 0 else idx[1]+1,\
   "s" if idx[1] < 0 else "n",\
   abs(idx[0]) if idx[0] < 0 else idx[0]+1,\
   "w" if idx[0] <0 else "e"\
)
left = lambda idx: (idx[0]-1, idx[1])
right = lambda idx: (idx[0]+1, idx[1])
up = lambda idx: (idx[0], idx[1]+1)
down = lambda idx: (idx[0], idx[1]-1)

url = lambda key, base_url, : '%s%d%s%d%s.png' % (base_url, key[0],key[1],key[2],key[3])
select_base = lambda idx: base_urls[1] if idx in custom_idxs else base_urls[0]
load_data = lambda conn: conn.read() if conn.code == 200 else None

# main loop
if __name__=='__main__':
	# Crawling images
	print "Crawling images"
	found = 0
	while stack:
		idx = stack.pop()
		u = url( tr( idx ), select_base( idx ))
		data = load_data( urllib.urlopen( u ))
		explored[idx] = data
		if data is not None:
			found += 1
			sys.stdout.write("\rImages found: %d" % found)
			sys.stdout.flush()
			for unexplored in filter( lambda i: i not in explored, [left(idx), right(idx), up(idx), down(idx)]):
				stack.append(unexplored)


		
	
	#big_image = Image.new('L',(width,height), 255)
	#for (x,y) in keys_with_data:
	#	data = explored[(x,y)]
	#	offset_x = (x - min_x)*image_size[0]
	#	offset_y = (max_y - y)*image_size[1]
	#	big_image.paste(data, (offset_x, offset_y))
	#big_image.save("big_xkcd.png")
		
	