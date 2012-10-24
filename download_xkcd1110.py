# https://raw.github.com/pantherhash/ph_1/master/download_xkcd.py
import urllib

# constants

base_url = 'http://imgs.xkcd.com/clickdrag/'
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
load_data = lambda conn: conn.read() if conn.code == 200 else None

# main loop
if __name__=='__main__':
	while stack:
		idx = stack.pop()
		u = url( tr( idx ), base_url)
		data = load_data( urllib.urlopen( u ))
		explored[idx] = data
		if data is not None:
			# print and save files to disc
			print "Found image", u
			imgfile = open("%d%s%d%s.png" % tr(idx), 'w')
			imgfile.write(data)
			imgfile.close()
			for unexplored in filter( lambda i: i not in explored, [left(idx), right(idx), up(idx), down(idx)]):
				stack.append(unexplored)
