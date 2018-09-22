from find_k_nearest_neighbours import find_k_nearest_neighbours

#4. list[float] calculate_outlieness(list[list[float]] points)
                 #->points have 5 dimensions
                 #->using find_k_nearest_neighbors function, calculate average of the distance and calculate outliness for all the points
                 #->return the outlieness of all correponding points

def calculate_outlieness(data, k = 200):
	outlieness = []

	for i in range(len(data)):
		distances = find_k_nearest_neighbours(data, i, k)
		total_distance = sum(claim[0] for claim in distances)
		outlieness.append(total_distance)
	
	return outlieness