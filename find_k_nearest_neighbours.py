from find_distance import find_distance

#3. list[[float, int]] find_k_nearest_neighbours(list[list[float]] points, int index1, int k);
                 #->using 5 dimensions and distance function, find nearest k points
                 #->output points' index

def find_k_nearest_neighbours(data, index, k=200):

	distances = []

	for i in range(len(data)):
		cur_distance = find_distance(data[index], data[i])
		distances.append([cur_distance, i])
	
	return sorted(distances, reverse=True)[:k]