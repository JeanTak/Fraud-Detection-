from calculate_outlieness import calculate_outlieness
import operator

#5. list[list[int and str]] top_100_providers(list[float] outlieness, list[list[float]] eight_dimensional_data);

def top_providers(outlieness, eight_dimensional_data):	
	provider_list = {}
	outlieness = calculate_outlieness(eight_dimensional_data)

	for i in range(len(outlieness)):
		provider_list[eight_dimensional_data[i][2]] += outlieness[i]

	sorted_list = sorted(provider_list.items(), key=operator.itemgetter(1), reverse=True)
	providers = sorted_list.keys()

	rank = []
	for i in range(len(providers)):
		rank.append([providers[i],i])
	
	return rank

	
		
	
