# Fraud-Detection

Unsupervised fraud detection algorithm:
1. Normalized distance
2. find k-nearest neighbours for all points
3. calculate outlieness for all points
4a.rank the providers
4b.rank the visits
 Functions:
1. list[list[double]] read_csv_file();
2. double find_distance(list[double] point1, list[double] point2)
                 ->calculate distance using normalized distance function
3. list[int] find_k_nearest_neighbours(list[list[double]] points, int index1, int k);
                 ->using 5 dimensions and distance function, find nearest k points
                 ->output points' index
4. list[double] calculate_outlieness(list[list[double]] data)
                 ->using find_k_nearest_neighbors function, calculate average of the distance and calculate outliness for all the points
5. list[int] top_10_providers(list[list]);
