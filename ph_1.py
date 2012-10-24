# https://raw.github.com/pantherhash/ph_1/master/ph_1.py
from PIL import Image
import urllib
import sys
from hashlib import sha1

# Approach 1: Run this program and print out the images.
# Approach 2: Don't run this program. The answer is in the code.

# celebs
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
start_node = (0, 0)
base_urls = {'xkcd':'https://raw.github.com/pantherhash/ph_1/master/xkcd_images/',\
             'celebs': 'https://raw.github.com/pantherhash/ph_1/master/celeb_images/'}
image_size = (2048, 2048)

# state
explored = {}
stack = [start_node]

# functions
_00_to_1n1e = lambda idx: (\
    abs(idx[1]) if idx[1] < 0 else idx[1]+1, "s" if idx[1] < 0 else "n",\
    abs(idx[0]) if idx[0] < 0 else idx[0]+1, "w" if idx[0] <0 else "e"\
)
left = lambda idx: (idx[0]-1, idx[1])
right = lambda idx: (idx[0]+1, idx[1])
up = lambda idx: (idx[0], idx[1]+1)
down = lambda idx: (idx[0], idx[1]-1)

# main loop
if __name__=='__main__':
	found = 0
	while stack:
		idx = stack.pop()
		xkcd_coord = _00_to_1n1e( idx )
		url = '%s%d%s%d%s.png' % (base_urls['xkcd'], key[0],key[1],key[2],key[3])   % (xkcd_coord, base)
		conn = urllib.urlopen( url )
		data = conn.read() if conn.code == 200 else None
		explored[idx] = data
		if data is not None:
			for unexplored in filter( lambda i: i not in explored, [left(idx), right(idx), up(idx), down(idx)]):
				stack.append(unexplored)

idxs_with_data = [k for (k,v) in filter(lambda item: item[1] is not None, explored.items())]
for idx in idxs_with_data:
	image = Image.new('RGB',image_size, (255,255,255))
	# Add coordinate (idx) to image
	
	# Add celeb to image?
	image.save("%d_%d.png" % (idx[0], idx[1]))
	
	#big_
	#for (x,y) in keys_with_data:
	#	data = explored[(x,y)]
	#	offset_x = (x - min_x)*image_size[0]
	#	offset_y = (max_y - y)*image_size[1]
	#	big_image.paste(data, (offset_x, offset_y))
	#big_image.save("big_xkcd.png")
		
	