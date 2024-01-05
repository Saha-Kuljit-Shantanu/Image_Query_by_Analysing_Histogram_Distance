from flask import Flask, send_from_directory,request,jsonify
from werkzeug.utils import secure_filename
from Image_Histogram_Extraction import extract_histogram_vector
from Get_Histogram_Distance_Sorted import get_histogram_distance_sorted


app = Flask(__name__)


#Connect Svelte public folder as root folder with Python Flask

@app.route("/")
def base():
    return send_from_directory('image-query/public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('image-query/public', path)

#Get image from route upload ,METHOD: POST

app.config['UPLOAD_FOLDER'] = 'uploads'
@app.route("/upload",methods = ['POST'])
def upload_file():

    try: 

        #Get uploaded image from route upload here (python flask) ,METHOD: POST

        file = request.files['image']
        
        #Give the image a filename and secure filename

        original_filename = file.filename
        
        filename = secure_filename(original_filename)
        
        #Retrieve the histogram vector from the collected image
        
        my_histogram_vector = extract_histogram_vector(file)
        
        my_histogram_list = get_histogram_distance_sorted(my_histogram_vector) 
    
        #Return the part of the sorted list to display in front end

        my_fragmented_histogram_list = my_histogram_list[:24]
        
        print( jsonify( {'image_list': my_histogram_list} ) )

        return jsonify( {'image_list': my_fragmented_histogram_list} )
    
    except:

        print("No file Uploaded")

        return jsonify( {'original_filename': None,
            'filename':  None} )

    


if __name__ == "__main__":
    app.run(debug=True)