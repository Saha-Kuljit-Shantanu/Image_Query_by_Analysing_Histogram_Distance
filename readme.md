# Image_Query_by_Analysing_Histogram_Distance

**Purpose :** Taking an image as input and get 24 best-fit images sorted by histogram distance with the Query image in ascending order

**Data Training :**
  - The histogram of the images in the folder **/image-query/public/Data** are already trained through the code **/Store_Image_Histogram.py**
  - The histogram of the images of the corresponding files has been stored in the csv file **/Histogram_file.csv**
  - Further images or image directories can be added to the folder **/image-query/public/Data** and the histograms of the images can be stored offline running the code **/Store_Image_Histogram.py** . The csv file **/Histogram_file.csv** gets updated automatically

**Data Testing :**
  - User will run necessary code following the instructions in the presentation file
  - Then the user has to navigate to the webpage **https://localhost:5000** (The listening port might vary from device to device, the server port is the port displayed while running the python file
  - Then the user has to click **Upload** button and this will open a pop-up window with all files in the computer
  - Then the user selects the image and clicks **Search** button 
