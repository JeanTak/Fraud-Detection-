from calculate_outlieness import calculate_outlieness

def top_types_claims(eight_dimensional_data): # data is partial
	outlieness = calculate_outlieness(eight_dimensional_data)
	outlieness_rank = [[]]
	
	for index in range(len(outlieness)):
		outlieness_rank.append([outlieness[index], index])

	outlieness_rank.sort(reverse=True)

	rank = []
	for i in range(len(outlieness_rank)):
		index = outlieness_rank[i][1]
		family_id = eight_dimensional_data[index][0]
		family_member_id = eight_dimensional_data[index][1]
		provider_id = eight_dimensional_data[index][2]
		date_of_service = eight_dimensional_data[index][5]
		provider_type = eight_dimensional_data[index][3]

		rank.append([family_id, family_member_id, provider_id, date_of_service, provider_type, i+1])
	
	return rank