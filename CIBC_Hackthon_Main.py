#main file

from read_csv_file import read_csv_file
from find_distance import find_distance
from find_k_nearest_neighbours import find_k_nearest_neighbours
from calculate_outlieness import calculate_outlieness
from top_providers import top_providers

all_points = [[]]
all_points = read_csv_file("5_dimension(200row)")
outlieness = []
outlieness = calculate_outlieness(all_points)

top_providers_list = [[]]
top_providers_list= top_providers(outlieness)