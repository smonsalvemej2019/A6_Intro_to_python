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

def summarystats(sepal_length, sepal_width, petal_length, petal_width):
    avg_sl, avg_sw = calculate_avg(sepal_length), calculate_avg(sepal_width)
    avg_pl, avg_pw = calculate_avg(petal_length), calculate_avg(petal_width)
    print("avg_sl ", avg_sl, "\navg_sw ", avg_sw, "\navg_pl ", avg_pl, "\navg_pw ", avg_pw)
    print()

    min_sl, min_sw = min(sepal_length), min(sepal_width)
    min_pl, min_pw = min(petal_length), min(petal_width)
    print("min_sl ", min_sl, "\nmin_sw ", min_sw, "\nmin_pl ", min_pl, "\nmin_pw ", min_pw)
    print()

    max_sl, max_sw = max(sepal_length), max(sepal_width)
    max_pl, max_pw = max(petal_length), max(petal_width)
    print("max_sl ", max_sl, "\nmax_sw ", max_sw, "\nmax_pl ", max_pl, "\nmax_pw ", max_pw)
    print()

    stdev_sl = calculate_stdev(sepal_length, avg_sl)
    print("stdev_sl ", stdev_sl)
    print()
    return 0

###############################################################################################
######################################## MAIN FUNCTION ########################################
fields = []
# setosa lists
seto_sepal_length, seto_sepal_width = [], []
seto_petal_length, seto_petal_width = [], []
# versicolor lists
vers_sepal_length, vers_sepal_width = [], []
vers_petal_length, vers_petal_width = [], []
# virginica lists
virg_sepal_length, virg_sepal_width = [], []
virg_petal_length, virg_petal_width = [], []

with open("iris.csv", 'r') as csvfile:
    reader = csv.reader(csvfile) # create csv reader object
    fields = next(reader) # get field names from first row

    # get each data row one by one
    for row in reader:
        if row[4] == "setosa":
            seto_sepal_length.append(float(row[0])) # get data from first col (sepal_length)
            seto_sepal_width.append(float(row[1])) # get data from second col (sepal_width)
            seto_petal_length.append(float(row[2])) # get data from third col (petal_length)
            seto_petal_width.append(float(row[3])) # get data from fourth col (petal_width)
        elif row[4] == "versicolor":
            vers_sepal_length.append(float(row[0]))
            vers_sepal_width.append(float(row[1]))
            vers_petal_length.append(float(row[2]))
            vers_petal_width.append(float(row[3]))
        else:
            virg_sepal_length.append(float(row[0]))
            virg_sepal_width.append(float(row[1]))
            virg_petal_length.append(float(row[2]))
            virg_petal_width.append(float(row[3]))

    summarystats(seto_sepal_length, seto_sepal_width, seto_petal_length, seto_petal_width)