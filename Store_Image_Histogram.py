from Image_Histogram_Extraction import extract_histogram_vector

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

histogram_file = open("Histogram_file.csv", "w")

for (dirpath, dirnames, filenames) in os.walk(dir_path + "\\image-query\\public\\Data"):

    for filename in filenames:

        filepath = os.path.join(dirpath,filename)

        filepath = str(filepath)
        
        image_histogram_vector = extract_histogram_vector(filepath)

        histogram_file.write(filepath)

        for pixel_value in image_histogram_vector :

            histogram_file.write(",")
            histogram_file.write(str(pixel_value))

        #histogram_file.write("\n")
        histogram_file.write("\n")

    #histogram_file.write("\n")

histogram_file.close()

    



