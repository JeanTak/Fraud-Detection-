from sklearn import neighbors
import math
def find_k_nearest_neighbours(data, index, k=200):
	distances = []
	tree = neighbors.KDTree(data, leaf_size = 400)
	for i in range(len(data)):
		cur_ds, indices = tree.query([data[i]], k)
		cur_distance = math.sqrt(cur_ds[0] * cur_ds[0] + cur_ds[1] * cur_ds[1] + cur_ds[2] * cur_ds[2])
		distances.append([cur_distance, i])
	return sorted(distances, reverse=True)[:k]