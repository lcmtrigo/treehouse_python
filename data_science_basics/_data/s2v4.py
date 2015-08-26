from s2v3 import *

def find_average(data_sample, header=False):
	total = calculate_sum(data_sample)
	size = number_of_records(data_sample)
	average = total / size
	return average

average_price = find_average(data_from_csv, True)
# print("Average = ", average_price)
# print('{:03.2f}'.format(average_price))
# print(average_price, int(average_price))
# print(type(int(average_price)))
# print(type(average_price))
# print(type(data_from_csv))
# print(type(my_csv))

midpoint = round(number_of_ties / 2)
message = "Average of {} half = ${:03.2f}"
# print(message.format("1st", find_average(data_from_csv[:midpoint], True)))
# print(message.format("2st", find_average(data_from_csv[midpoint:], False)))