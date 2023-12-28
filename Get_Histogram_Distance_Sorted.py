import csv
from math import sqrt

filename = 'Histogram_file.csv'

def get_histogram_distance_sorted(query_histogram_vector) :

    #Initialize an empty list of histogram distance

    histogram_distance_list = list()

    with open(filename) as csvfile:

        csv_reader = csv.reader(csvfile)

        #Read each row from the csv file
        for row in csv_reader:

            #Initialize histogram distance

            histogram_distance = 0

            #Loop for each histogram cell in the row to the Query histogram vector

            for i in range(0,256,1): 

                #Update histogram distance
                    
                histogram_distance = histogram_distance + (query_histogram_vector[i] - float( row [i+1] ))* (query_histogram_vector[i] - float( row [i+1] ))

            #Update histogram distance
                
            histogram_distance = sqrt(histogram_distance)

            #Create a tuple of image path and histogram distance from the query image

            image_tuple = (row[0], histogram_distance)

            #Append the tuple to the histogram list

            histogram_distance_list.append(image_tuple)

    #Sort the list and return to the back end

    histogram_distance_list.sort(key = lambda tup: tup[1])

    return histogram_distance_list
        