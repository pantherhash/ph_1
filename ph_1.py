# https://raw.github.com/pantherhash/ph_1/master/ph_1.py
from PIL import Image
import urllib
import sys

# constants

image_size = (2048, 2048)
base_urls = ['https://raw.github.com/pantherhash/ph_1/master/xkcd_images/',\
             'https://raw.github.com/pantherhash/ph_1/master/custom_images/']
custom_idxs = []#(0,0), (1,5),(-4,0)]
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
	# find min/max idx
	print "Finding minimum and maximum indexes"
	min_x, max_x, min_y, max_y = (0,0,0,0)
	keys_with_data = [k for (k,v) in filter(lambda item: item[1] is not None, explored.items())]
	for (x,y) in keys_with_data:
			min_x = min(min_x, x)
			max_x = max(max_x, x)
			min_y = min(min_y, y)
			max_y = max(max_y, y)
	print "\t",min_x, max_x, min_y, max_y
	
	lines = []
	ys = range(min_y, max_y)
	ys.reverse()
	for y in ys:
		line = []
		for x in range(min_x, max_x):
			line.append("*" if (x,y) in keys_with_data else " ")
		output_line = "".join(line)
		lines.append(output_line)

	overview = open("xkcd_overview_map.txt","w")
	for line in lines:		
		overview.write(line)
		overview.write("\n")
	overview.close()	
		
	print "Determining image dimensions"
	width, height = (max_x-min_x)*image_size[0], (max_y-min_y)*image_size[1]
	print "\t",width,height
	
	#big_image = Image.new('L',(width,height), 255)
	#for (x,y) in keys_with_data:
	#	data = explored[(x,y)]
	#	offset_x = (x - min_x)*image_size[0]
	#	offset_y = (max_y - y)*image_size[1]
	#	big_image.paste(data, (offset_x, offset_y))
	#big_image.save("big_xkcd.png")
		
	