import sys
import humanfriendly

fp = open(sys.argv[1], 'r')

for line in fp:
	n = ~int(line, 16) & 0xffffffffffff
	t = n#humanfriendly.format_size(n, binary=True)
	print t


