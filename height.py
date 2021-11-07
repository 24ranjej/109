import pandas as pd 
import statistics
import csv 

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

#mean for weight and height
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

#meadian for weight and height
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

#mode for height and weight
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

#printing mean, median, mode, to validate
print("Mean, Median, and Mode of height is {}, {}, and {} respectivly".format(height_mean, height_median, height_mode))
print("Mean, Median, and Mode of weight is {}, {}, and {} respectivly".format(weight_mean, weight_median, weight_mode))

#standard diviation for height and weight
height_std_diviation = statistics.stdev(height_list)
weight_std_diviation = statistics.stdev(weight_list)

#1,2,3 standard dviation for height
height_first_std_diviation_start, height_first_std_diviation_end = height_mean-height_std_diviation, height_mean+height_std_diviation
height_second_std_diviation_start, height_second_std_diviation_end = height_mean-(2*height_std_diviation), height_mean+(2*height_std_diviation)
height_third_std_diviation_start, height_third_std_diviation_end = height_mean-(3*height_std_diviation), height_mean+(3*height_std_diviation)

#1,2,3 standard dviation for weight
weight_first_std_diviation_start, weight_first_std_diviation_end = weight_mean-weight_std_diviation, weight_mean+weight_std_diviation
weight_second_std_diviation_start, weight_second_std_diviation_end = weight_mean-(2*weight_std_diviation), weight_mean+(2*weight_std_diviation)
weight_third_std_diviation_start, weight_third_std_diviation_end = weight_mean-(3*weight_std_diviation), weight_mean+(3*weight_std_diviation)

#percentage of data within 1,2,3 standard divaition for height
height_list_of_data_within_1_std_diviation = [result for result in height_list if result > height_first_std_diviation_start and result < height_first_std_diviation_end]
height_list_of_data_within_2_std_diviation = [result for result in height_list if result > height_second_std_diviation_start and result < height_second_std_diviation_end]
height_list_of_data_within_3_std_diviation = [result for result in height_list if result > height_third_std_diviation_start and result < height_third_std_diviation_end]

#percentage of data within 1,2,3 standard divaition for height
weight_list_of_data_within_1_std_diviation = [result for result in weight_list if result > weight_first_std_diviation_start and result < weight_first_std_diviation_end]
weight_list_of_data_within_2_std_diviation = [result for result in weight_list if result > weight_second_std_diviation_start and result < weight_second_std_diviation_end]
weight_list_of_data_within_3_std_diviation = [result for result in weight_list if result > weight_third_std_diviation_start and result < weight_third_std_diviation_end]

#printing data for height and weight (standard diviation)
print("{}% of data for height lies within 1 standard diviation".format(len(height_list_of_data_within_1_std_diviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard diviation".format(len(height_list_of_data_within_2_std_diviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard diviation".format(len(height_list_of_data_within_3_std_diviation)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard diviation".format(len(weight_list_of_data_within_1_std_diviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard diviation".format(len(weight_list_of_data_within_2_std_diviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard diviation".format(len(weight_list_of_data_within_3_std_diviation)*100.0/len(weight_list)))

