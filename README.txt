# Fraud-Detection

Unsupervised fraud detection algorithm:
1. Normalized distance
2. find k-nearest neighbours for all points
3. calculate outlieness for all points
4a.rank the providers
4b.rank the visits


 Functions:
1. list[list[float]] read_csv_file(string filename);
2. float find_distance(list[float] point1, list[float] point2)
                 ->calculate distance using normalized distance function
3. list[int] find_k_nearest_neighbours(list[list[float]] points, int index1, int k);
                 ->using 5 dimensions and distance function, find nearest k points
                 ->output points' index
4. list[float] calculate_outlieness(list[list[float]] points, list[list[float]] 7_dimensional_data)
                 ->points have 5 dimensions
                 ->using find_k_nearest_neighbors function, calculate average of the distance and calculate outliness for all the points
                 ->return the outlieness of all correponding points
5. list[list[int and str]] top_providers(list[float] outlieness);
6. list[list[int and str]] top_100_visits(list[float] outlieness);

Files:

"Full_file"
"5_dimensional"

"Full_file(200row)"
"5_dimensional(200row)"

"Full_file(2000row)"
"5_dimensional(2000row)"

"Full_file(200000row)"
"5_dimensional(200000row)"
