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

# store the summary statistics for each species in a nested dictionary
iris_summary = {
    "setosa" : {
        # "attribute_name" = [min, max, mean, stdev]
        "sepal_length": [], "sepal_width": [],
        "petal_length": [], "petal_width": [],
    },
    "versicolor" : {
        # "attribute_name" = [min, max, mean, stdev]
        "sepal_length": [], "sepal_width": [],
        "petal_length": [], "petal_width": [],
    },
    "virginica" : {
        # "attribute_name" = [min, max, mean, stdev]
        "sepal_length": [], "sepal_width": [],
        "petal_length": [], "petal_width": [],
    }
}


def calculate_avg(attribute_list):
    return sum(attribute_list)/len(attribute_list) # sum / (# of flowers)


def calculate_stdev(attribute_list, mean):
    var = sum((x - mean) ** 2 for x in attribute_list) / len(attribute_list) # calculate variance
    std_dev = math.sqrt(var)
    return std_dev


def summarystats(species_name, species):
    # print("species ", species)

    for attribute in species.keys():
        # print("attribute ", attribute)
        mini = min(species[attribute])
        maxi = max(species[attribute])
        avg = calculate_avg(species[attribute])
        stdev = calculate_stdev(species[attribute], avg)
        iris_summary[species_name][attribute] = [mini, maxi, avg, stdev]

    print(iris_summary[species_name])

def summarystats_table():
    # print 3 4x4 tables (3 because 1 for each species)
    return 0
    

###############################################################################################
######################################## MAIN FUNCTION ########################################
fields = []
# store information regarding the four attributes for each species in a nested dictionary
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

    summarystats("setosa", iris["setosa"])


