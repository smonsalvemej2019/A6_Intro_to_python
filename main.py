###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###          Assignment 6: EDA for the Iris Dataset                     ###
###          Group Members:                                             ###
###          Name: Humyra Chowdhury            Z#: 23405864             ###
###          Name: Weiyi Huang                 Z#:                      ###
###          Name: Santiago Monsalve-Mejia     Z#:                      ###
###          Date: Jul 09, 2021                                         ###
### Description: expand and strengthen understanding of lists, tuples,  ###
### functions, dictionaries, and CSV file manipulation to perform       ###
### simple Exploratory Data Analysis (EDA) of the Iris flower dataset.  ###
###########################################################################
import csv
import math


def calculate_avg(attribute_list):
    return sum(attribute_list)/len(attribute_list) # sum / (# of flowers)


def calculate_stdev(attribute_list, mean):
    var = sum((x - mean) ** 2 for x in attribute_list) / len(attribute_list) # calculate variance
    std_dev = math.sqrt(var)
    return std_dev


def summarystats(species):
    # find the min
    min_sl, min_sw = min(species["sepal_length"]), min(species["sepal_width"])
    min_pl, min_pw = min(species["petal_length"]), min(species["petal_width"])
    print("min_sl ", min_sl, "\nmin_sw ", min_sw, "\nmin_pl ", min_pl, "\nmin_pw ", min_pw)
    print()

    # find the maximum
    max_sl, max_sw = max(species["sepal_length"]), max(species["sepal_width"])
    max_pl, max_pw = max(species["petal_length"]), max(species["petal_width"])
    print("max_sl ", max_sl, "\nmax_sw ", max_sw, "\nmax_pl ", max_pl, "\nmax_pw ", max_pw)
    print()

    # find the mean
    avg_sl, avg_sw = calculate_avg(species["sepal_length"]), calculate_avg(species["sepal_width"])
    avg_pl, avg_pw = calculate_avg(species["petal_length"]), calculate_avg(species["petal_width"])
    print("avg_sl ", avg_sl, "\navg_sw ", avg_sw, "\navg_pl ", avg_pl, "\navg_pw ", avg_pw)
    print()

    # find the standard deviation
    stdev_sl, stdev_sw = calculate_stdev(species["sepal_length"], avg_sl), calculate_stdev(species["sepal_width"], avg_sw)
    stdev_pl, stdev_pw = calculate_stdev(species["petal_length"], avg_pl), calculate_stdev(species["petal_width"], avg_pw)
    print("stdev_sl ", stdev_sl, "\nstdev_sw ", stdev_sw, "\nstdev_pl ", stdev_pl, "\nstdev_pw ", stdev_pw)
    print()


def summarystats_table():
    # print 3 4x4 tables (3 because 1 for each species)
    return 0
    

###############################################################################################
######################################## MAIN FUNCTION ########################################
fields = []
iris = {
    "setosa" : {
        "sepal_length": [], "sepal_width": [],
        "petal_length": [], "petal_width": [],
    },
    "versicolor" : {
        "sepal_length": [], "sepal_width": [],
        "petal_length": [], "petal_width": [],
    },
    "virginica" : {
        "sepal_length": [], "sepal_width": [],
        "petal_length": [], "petal_width": [],
    }
}

with open("iris.csv", 'r') as csvfile:
    reader = csv.reader(csvfile) # create csv reader object
    fields = next(reader) # get field names from first row

    # get each data row one by one
    for row in reader:
        if row[4] == "setosa":
            iris["setosa"]["sepal_length"].append(float(row[0])) # get data from first col (sepal_length)
            iris["setosa"]["sepal_width"].append(float(row[1])) # get data from second col (sepal_width)
            iris["setosa"]["petal_length"].append(float(row[2])) # get data from third col (petal_length)
            iris["setosa"]["petal_width"].append(float(row[3])) # get data from fourth col (petal_width)

    summarystats(iris["setosa"])


