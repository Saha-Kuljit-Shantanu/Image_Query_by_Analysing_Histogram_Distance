# Image_Query_by_Analysing_Histogram_Distance

**Purpose :** Taking an image as input and get 24 best-fit images sorted by histogram distance with the Query image in ascending order

**Data Training :**
  - The histogram of the images in the folder **/image-query/public/Data** are already trained through the code **/Store_Image_Histogram.py**
  - The histogram of the images of the corresponding files has been stored in the csv file **/Histogram_file.csv**
  - Further images or image directories can be added to the folder **/image-query/public/Data** and the histograms of the images can be stored offline running the code **/Store_Image_Histogram.py** . The csv file **/Histogram_file.csv** gets updated automatically

**Data Testing :**
  - User will run necessary code following the instructions in the presentation file **How to Run this project.pptx**
  - Then the user has to navigate to the webpage **https://localhost:5000** ( The listening port might vary from device to device, the server port is the port displayed while running the python file **Flask-Server.py** )
  - Then the user has to click **Upload** button and this will open a pop-up window with all files in the computer
  - Then the user selects the image and clicks **Search** button

**How to run this Project ?**
  - Although a detailed procedure is explained in file **How to Run this project.pptx**, here i a quick precap
  - Open the entire folder **Image_Query_by_Analysing_Histogram_Distance** as a project in any text editor and navigate to this folder in terminal
  - If **Flask** is not installed, then it needs to be installed :
      - **pip install flask**
  - If **PIL (Python Image Library)** is not installed, then it needs to be installed :
      - **pip install PIL**
  - Open two terminals
  - In the first terminal put the following commands sequentially :
      - **cd image-query**
      - **npm install** (Only the first time to install dependencies)
      - **npm run dev**
  - In the second terminal run **/Flask-Server.py**
