#main file
from read_csv_file import read_csv_file
from find_distance import find_distance
from find_k_nearest_neighbours import find_k_nearest_neighbours
from calculate_outlieness import calculate_outlieness
from top_providers import top_providers
import csv
import globalvar



five_dimensional_points = [[]]
eight_dimensional_points = [[]]
five_dimensional_points = read_csv_file("5_dimensional(20000row).csv")
eight_dimensional_points = read_csv_file("Full_file(20000row).csv")

#find high or low bound for distance function

globalvar.pl = 0
globalvar.ph = 0
globalvar.dh = 0
globalvar.dl = 0

for points in five_dimensional_points:
	globalvar.ph = max(points[3], globalvar.ph)
	globalvar.pl = min(points[3], globalvar.pl)
	globalvar.dh = max(points[4], globalvar.dh)
	globalvar.dl = min(points[4], globalvar.dl)


outlieness = []
outlieness = calculate_outlieness(five_dimensional_points)

top_providers_list = [[]]
top_providers_list = top_providers(outlieness, eight_dimensional_points)

with open('provider.csv', 'wb') as f:  # Just use 'w' mode in 3.x
	w = csv.writer(f)
	w.writerows(top_providers_list)