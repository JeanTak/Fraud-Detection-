#main file
from read_csv_file import read_csv_file
from find_distance import find_distance
from find_k_nearest_neighbours import find_k_nearest_neighbours
from calculate_outlieness import calculate_outlieness
from top_providers import top_providers
from top_types import top_types_claims
import csv
import globalvar

five_dimensional_points = [[]]
eight_dimensional_points = [[]]
top_claims_list = [[]]

for count in range(5,12):
	five_dimensional_points = []
	eight_dimensional_points=[]
	five_dimensional_points = read_csv_file("provider_type"+str(count+1)+".csv")
	eight_dimensional_points = read_csv_file("provider_type"+str(count+1)+".csv")

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

	top_claims_list += top_types_claims(eight_dimensional_points)

with open('type_result'+str(count)+'.csv', 'wb') as f:  # Just use 'w' mode in 3.x
		w = csv.writer(f)
		w.writerows(top_claims_list)