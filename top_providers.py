from calculate_outlieness import calculate_outlieness
#5. list[list[int and str]] top_100_providers(list[float] outlieness, list[list[float]] eight_dimensional_data);

def top_providers(outlieness, eight_dimensional_data):	
	provider_list = {}
	outlieness = calculate_outlieness(eight_dimensional_data)

	for i in range(len(eight_dimensional_data)):
		provider_list[eight_dimensional_data[i][2]] += 1
	
	sorted(provider_list, key = lambda x: x[1], reverse=True)

	rank = {key: rank for rank, key in enumerate(sorted(provider_list, key=provider_list.get, reverse=True), 1)}	
	return rank

	
		
	
