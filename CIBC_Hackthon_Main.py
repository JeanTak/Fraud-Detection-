#main file
from read_csv_file import read_csv_file
from find_distance import find_distance
from find_k_nearest_neighbours import find_k_nearest_neighbours
from calculate_outlieness import calculate_outlieness
from top_providers import top_providers
import csv

five_dimensional_points = [[]]
eight_dimensional_points = [[]]
five_dimensional_points = read_csv_file("5_dimension(200row)")
eight_dimensional_points = read_csv_file("Full_file(200row)")

outlieness = []
outlieness = calculate_outlieness(five_dimensional_points)

top_providers_list = {}
top_providers_list = top_providers(outlieness, eight_dimensional_points)

with open('provider.csv', 'wb') as f:  # Just use 'w' mode in 3.x
	w = csv.DictWriter(f, top_providers_list.keys())
	w.writeheader()
	w.writerow(top_providers_list)

