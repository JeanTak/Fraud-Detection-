# Fraud-Detection

Unsupervised fraud detection algorithm:
1. Normalized distance
2. find k-nearest neighbours for all points
3. calculate outlieness for all points
4a.rank the providers
4b.rank the visits


 Functions:
1. list[list[double]] read_csv_file(string filename);
2. double find_distance(list[double] point1, list[double] point2)
                 ->calculate distance using normalized distance function
3. list[int] find_k_nearest_neighbours(list[list[double]] points, int index1, int k);
                 ->using 5 dimensions and distance function, find nearest k points
                 ->output points' index
4. list[double] calculate_outlieness(list[list[double]] data)
                 ->using find_k_nearest_neighbors function, calculate average of the distance and calculate outliness for all the points
5. list[list[int and str]] top_100_providers(list[double]);
6. list[list[int and str]] top_100_visits(list[double]);

Files:

"Full_file"
"5_dimensional"

"Full_file(200row)"
"5_dimensional(200row)"

"Full_file(2000row)"
"5_dimensional(2000row)"

"Full_file(200000row)"
"5_dimensional(200000row)"
