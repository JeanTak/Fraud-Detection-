import math

def find_distance(point_1, point_2):
#     c1 = calc_distance([100, 100, 1000, 1000])
    c1 = calc_distance([pl, dl, ph, dh])
    return (c1.euclidean_distance(point_1, point_2))

class calc_distance:
    def __init__(self, bd_list):
        self.bound_list = bd_list

    # def chi_square_distance(point_1, point_2, bound_list):
    def euclidean_distance(self, point_1, point_2):
        sum = 0
        for i in range(5):
            if i == 3 or i == 4:
                sum += (self.linear_mapping(point_1[i], self.bound_list[i-3], self.bound_list[i-1]) 
                        - self.linear_mapping(point_2[i], self.bound_list[i-3], self.bound_list[i-1])) ** 2
            elif point_1[i] != point_2[i]:
                sum += 50 ** 2
            # print (sum)
        return math.sqrt(sum)

    def linear_mapping(self, data, lower_bound, upper_bound):
        return (data - lower_bound) / (upper_bound - lower_bound) * 100
