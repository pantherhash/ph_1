# https://raw.github.com/pantherhash/ph_1/master/download_xkcd.py
import urllib
import sys

# constants

base_url = 'http://imgs.xkcd.com/clickdrag/'
start_node = (0, 0)
image_size = (2048, 2048)

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
load_data = lambda conn: conn.read() if conn.code == 200 else None

# main loop
print "Using depth first search to crawl Click and Drag"
found = 0
if __name__=='__main__':
	while stack:
		idx = stack.pop()
		u = url( tr( idx ), base_url)
		data = load_data( urllib.urlopen( u ))
		explored[idx] = data
		if data is not None:
			# print and save files to disc
			found += 1
			sys.stdout.write("\rImages found: %d" % found)
			sys.stdout.flush()
			imgfile = open("%d%s%d%s.png" % tr(idx), 'w')
			imgfile.write(data)
			imgfile.close()
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


# print image dimensions
print "Determining dimensions"
width, height = (max_x-min_x)*image_size[0], (max_y-min_y)*image_size[1]
print "\t",width,height

# print and save map
print "Creating ASCII-art map"
lines = []
ys = range(min_y, max_y)
ys.reverse()
for y in ys:
	line = []
	for x in range(min_x, max_x):
		line.append("*" if (x,y) in keys_with_data else " ")
	output_line = "".join(line)
	lines.append(output_line)

ascii_map = open("xkcd1110_map.txt","w")
for line in lines:
	print line
	ascii_map.write(line)
	ascii_map.write("\n")
ascii_map.close()