###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###          Assignment 6: EDA for the Iris Dataset                     ###
###          Group Members:                                             ###
###          Name: Humyra Chowdhury            Z#: 23405864             ###
###          Name: Weiyi Huang                 Z#: 23502284             ###
###          Name: Santiago Monsalve-Mejia     Z#:                      ###
###          Date: Jul 09, 2021                                         ###
### Description: expand and strengthen understanding of lists, tuples,  ###
### functions, dictionaries, and CSV file manipulation to perform       ###
### simple Exploratory Data Analysis (EDA) of the Iris flower dataset.  ###
###########################################################################

import csv
import statistics

def open_csv_file():

      with open("iris.csv", "r") as f: ## Open the csv file
         reader = csv.reader(f)    ## Read file
         next(reader) ## Skip the first row
         data = []

         for row in reader:
             data.append(row) ## Collect all data rows
      
      normalization(data) ## Call the normalization function
      decision_tree(data)
       
     
def normalization(data):
    ## Create four empty list
    datalist1 = []
    datalist2 = []
    datalist3 = []
    datalist4 = []
    ## Append each row to one of each empty list
    for row in data:
        datalist1.append(float(row[0]))
        datalist2.append(float(row[1]))
        datalist3.append(float(row[2]))
        datalist4.append(float(row[3]))
    ## Create variables for hold the min & max values of each list
    minimun1,maximun1 = min(datalist1),max(datalist1)
    minimun2,maximun2 = min(datalist2),max(datalist2)
    minimun3,maximun3 = min(datalist3),max(datalist3)
    minimun4,maximun4 = min(datalist4),max(datalist4)

    normalize_sepal_length = [(a - minimun1) / (maximun1 - minimun1)for a in datalist1]
    normalize_sepal_width = [(a - minimun2) / (maximun2 - minimun2)for a in datalist2]

    normalize_petal_length = [(a - minimun3) / (maximun3 - minimun3)for a in datalist3]
    normalize_petal_width = [(a - minimun4) / (maximun4 - minimun4)for a in datalist4]

    print(75 * "-")
    print(5 * "-", "Summary (iris_norm)", 5 *"-")
    print(75 * "-")
    print(f'{"Attributes (cm)":<20} {"Sepal Length":>14} {"Sepal Width": >19} {"Petal Length":>20} {"Petal Width":>20}')
    print(75 * "-")
    print(
        f'{"Min: ":<20} {min(normalize_sepal_length):>10.4f} {min(normalize_sepal_width):>20.4f}'
        f'{min(normalize_petal_length):>20.4f} {min(normalize_petal_width):>20.5f}')
    print(
        f'{"Mean: ":<20} {statistics.mean(normalize_sepal_length):>10.4f} {statistics.mean(normalize_sepal_width):>20.4f}'
        f'{statistics.mean(normalize_petal_length):>20.4f} {statistics.mean(normalize_petal_width):>20.5f}')
    print(
        f'{"Max: ":<20} {max(normalize_sepal_length):>10.4f} {max(normalize_sepal_width):>20.4f}'
        f'{max(normalize_petal_length):>20.4f} {max(normalize_petal_width):>20.5f}')

def decision_tree(data):
    ## Create two empty list
    datalist1 = []
    datalist2 = []

    setosa = 0
    versicolor = 0 
    virginica = 0

    for row in data:
        datalist1.append(float(row[2]))
        datalist2.append(float(row[3]))

    for i in range(len(data)):
        petal_length = datalist1[i]
        petal_width = datalist2[i]

        if 0.5 < petal_length < 2.5 :
            setosa = setosa + 1
        
        else:
            if 2.5 < petal_length < 5.2:
                if 0.8 < petal_width < 2.4:
                    versicolor = versicolor + 1
            elif 4.6 < petal_length < 7.0:
                if 1.6 < petal_width < 2.7:
                    virginica = virginica + 1
    
    sum = setosa + versicolor + virginica
    setosa_percentage = (setosa / sum) * 100
    versicolor_percentage = (versicolor / sum) * 100
    virginica_percentage = (virginica / sum) * 100
    print(100 * "-")
    print(40 * "-","Decision Tree", 40 * "-")
    print("setosa = ", setosa, ", percentage:", round(setosa_percentage, 2),"%")
    print("versicolor = ", versicolor, ", percentage:", round(versicolor_percentage, 2),"%")
    print("virginica = ", virginica, ", percentage:", round(virginica_percentage, 2),"%")


open_csv_file()
  
