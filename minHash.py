from datasketch import MinHash
from collections import defaultdict
import os
import pickle
## store filenames in an array

filenames = os.listdir("./")
## iterate through this array, do minhash
for filename in filenames:
	cur_file = open(filename,'r')
	cur_ids = cur_file.read().split('\n')
	cur_file.close()

## store minhash list into pickle
def minhash_IDs(IDs):
	m = MinHash()
	for ID in IDs:
		m.update(d.encode('utf-8'))
def store_minhash(data, file_name):
	data = [1,2,3]
	f = open(file_name, "wb")
	pickle.dump(data, f)
if __name__ == "__main__":
	print("hello")
'''
https://ekzhu.github.io/datasketch/minhash.html
https://blog.csdn.net/lsq2902101015/article/details/51305825
https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p21_serializing_python_objects.html
https://blog.csdn.net/Lycoridiata/article/details/78536768
'''