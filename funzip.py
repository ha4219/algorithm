
# fenwick
def tree_update(i,diff):
	while i<=N:
		tree[i]+=diff
		i+=i&-i
def tree_sum(i):
	r=0
	while i:
		r+=tree[i]
		i&=i-1
	return r