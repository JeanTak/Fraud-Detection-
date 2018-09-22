from calculate_outlieness import calculate_outlieness
import operator

#5. list[list[int and str]] top_100_providers(list[float] outlieness, list[list[float]] eight_dimensional_data);

def top_providers(outlieness, eight_dimensional_data):	
	provider_list = {}
	outlieness = calculate_outlieness(eight_dimensional_data)

	for i in range(len(outlieness)):
		if (provider_list.get(eight_dimensional_data[i][2]) is None):
			provider_list[eight_dimensional_data[i][2]] = outlieness[i]
		else:
			provider_list[eight_dimensional_data[i][2]] += outlieness[i]

	sorted_list = sorted(provider_list.items(), key=operator.itemgetter(1), reverse=True)

	rank = []
	for i in range(len(sorted_list)):
		rank.append([sorted_list[i][0],i+1])
	
	return rank

	
		
	
