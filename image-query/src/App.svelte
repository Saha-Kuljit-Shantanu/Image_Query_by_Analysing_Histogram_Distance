<script>

    
    //import {myVarList} from '/Image_Query_by_Analysing_histogram/image-query/public/store'
    
    let imageInput;
    let my_image_file = ''
    let files;
    let imageInFrame = localStorage.getItem('imageInFrame');
    let imageSelectFlag = 1;
    let imageOutputFlag = 0;
    let imageOutput;

    

    /** @type {HTMLInputElement}*/


    // export const snapshot = {

    //     capture: () => {return imageInput.files},
    //     restore: (files) => imageInput.files = files
    // };

     

    // Update the store when needed
    // function updateVariableList(newImageValue) {
    //     myVarList.set(newImageValue);
    // }



    // Function to derive a relative path
    function getRelativePath(absolutePath) {
        
        const imagePathParts = absolutePath.split('\\');
        let relativePath = imagePathParts.slice(imagePathParts.indexOf('Data')).join('/');
        relativePath = 'http://localhost:5000/' + relativePath
        //console.log(relativePath)

        return relativePath;
   }

   function chunkArray(arr, size) {
        const result = [];
        for (let i = 0; i < arr.length; i += size) {
            result.push(arr.slice(i, i + size));
         }
        return result;
   }

    function getBase64(image) {
        imageSelectFlag = 0;
        const reader = new FileReader();

        my_image_file = image;
        reader.readAsDataURL(image);
        reader.onload = e => {
            imageSelectFlag = 1;
            imageInFrame = e.target.result;

            localStorage.setItem('imageInFrame',imageInFrame)

            //localStorage.setItem('image',reader.result)

            
            //myVarList.set(imageInFrame);

            // myVarList.subscribe(imageValue => {
            //     imageInFrame = imageValue;
            // }) 
        };
    };

	const handleSearch = async () => {

        if(my_image_file == '' && imageInFrame != null) {
            var base64 = localStorage.getItem('imageInFrame')
            var base64parts = base64.split(",")
            var fileformat = base64parts[0].split(";")[0];
            var fileExt = fileformat.split("/")[1]
            var fileContent = base64parts[1];
            var bstr = atob(fileContent)
            var n = bstr.length
            var blob = new Uint8Array(n)

            while(n--){

                blob[n] = bstr.charCodeAt(n)
            }
            my_image_file = new File([blob],"a."+fileExt,{type : fileformat.split(":")[1]})

            console.log(fileformat)
            console.log(my_image_file)

        }

    
    const formData = new FormData();
    formData.append('image', my_image_file);

    
    console.log(my_image_file)
    


    try {

      imageOutputFlag = 0
      const response = await fetch('./upload', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      console.log(data);

      imageOutput = chunkArray(data.image_list,3)

      //$page.imageOutput = imageOutput;

      //$page.page.router.push('/1');

    //   const relativePath = getRelativePath(imageOutput[0][0]);

        
       console.log(localStorage.getItem('imageInFrame'))

    //   console.log(imageOutput[0])


      imageOutputFlag = 1


    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };
</script>

<div>

<div class="container">
    
    {#if imageInFrame != null}
        <div id="frame">
            
            {#if imageSelectFlag === 1 }
                <img id="image_layer" src={imageInFrame} alt="uploaded_image"/>
            {/if}
            <img id="frame_layer" src="/frame.gif" alt="frame"/>
        </div>
        
    {:else}

        <img id="frame" src= "/frame.gif" alt="frame"/>
        
    {/if}
       
    <input class="hidden" id="file-to-upload" name= "image" type="file" accept=".png,.jpg,.gif" bind:files bind:this={imageInput} on on:change={() => getBase64(files[0])}/>
    <div class = "button-holder">
        <button class="upload-btn" on:click= { () => imageInput.click() }>Upload</button>
        <button class="upload-btn" on:click= {handleSearch} >Search</button>
    </div>

    
</div>
    

<!-- <div> -->

    {#if imageOutputFlag === 1}

         
    {#each imageOutput as imageChunk, index(imageChunk)} 

        <div class="container">

            {#each imageChunk as image, index(image)}
                <div class = "image-container">
                    <a href={getRelativePath(image[0])}><img id="result_image_layer" src={getRelativePath(image[0])} alt={image[0]}/></a>
            
                    <p> Histogram Distance : {image[1]}</p>
                </div>
        
            {/each}

        </div>
        
    {/each} 

    {/if} 

<!-- </div> -->

</div>   



<style>
    .container {
        display: flex;
        /*flex-direction: column;
        /*align-items: center;*/

        position: relative;
    }

    #frame {
        /*border-radius: 99999px;*/
        height: 512px;
        width: 512px;
        margin-bottom: 10px;
        /*overflow: hidden;*/
        position : relative;
    }

    #frame_layer {
        /*border-radius: 99999px;*/
        height: 512px;
        width: 512px;
        margin-bottom: 10px;
        /*overflow: hidden;*/
        position : absolute;
    }

    #image_layer {
        /*border-radius: 99999px;*/
        height: 390px;
        width: 390px;
        margin-bottom: 10px;
        margin-top: 75px;
        margin-left: 65px;
        /*overflow: hidden;*/
        position : absolute;
    }

    #result_image_layer {
        /*border-radius: 99999px;*/
        height: 390px;
        width: 390px;
        border: 2px black;
        margin-bottom: 50px;
        margin-top: 50px;
        margin-left: 65px;
        
        /* border-top: 5px ;
		border-left: 5px ;
		border-right: 5px ;
		border-bottom: 5px ; */
        /*overflow: hidden;*/
        
    }

    .hidden {
        display: none;
    }

    .button-holder {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 512px;
        justify-content: center;
        gap: 20px;
    
    }

    .image-container {
        /* display: flex; */
        /*flex-direction: column;*/
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        position: relative;
    }

    .upload-btn {
        width: 256px;
        height: 32px;
        background-color: black;
        font-family: sans-serif;
        color: white;
        font-weight: bold;
        border: none;
    }

    .upload-btn:hover {
        background-color: white;
        color: black;
        outline: black solid 2px;
    }
</style>