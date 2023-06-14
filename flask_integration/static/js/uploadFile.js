let fileInput = document.getElementById("file-input");
let fileList = document.getElementById("files-list");
let numOfFiles = document.getElementById("num-of-files");
fileInput.addEventListener("change", () => {
  fileList.innerHTML = "";
  numOfFiles.textContent = ``;
  for (i of fileInput.files) {
    let reader = new FileReader();
    let listItem = document.createElement("li");
    listItem.addEventListener("click", function() { /* delete item functionality */
    listItem.remove();
    console.log("fileList", document.getElementById("files-list").getElementsByTagName("li").length);
    delete listItem;
   
  });
    let fileName = i.name;
    let fileSize = (i.size / 1024).toFixed(1);
    listItem.innerHTML = `<p>${fileName}</p>`;
    //listItem.innerHTML = `${fileName}<span class="close">&times;</span>`;
    /*if (fileSize >= 1024) {
      fileSize = (fileSize / 1024).toFixed(1);
      listItem.innerHTML = `<p>${fileName}</p>`;
    }*/
    fileList.appendChild(listItem);
    console.log("fileList", fileList);
  }

});


function validateFileType() {
        var inputElement = document.getElementById('file-input');

        //Get the file upload by user
        var files = inputElement.files;
        //Get the predicted class name for the model
        var predictedClassName = document.getElementById('className').value;

        if(files.length==0){
          alert("Please choose a file first...");
          return false;
        }


        else if(predictedClassName.length == 0 ){
            alert("Please enter the predicted column name first...");
            return false;
        }

        else{
          var filename = files[0].name;
          console.log("filename", filename);
          /* getting file extenstion eg- .jpg,.png, etc */
          var extension = filename.substr(filename.lastIndexOf("."));
          /* define allowed file types */
          var allowedExtensionsRegx = /(\.csv)$/i;
          /* testing extension with regular expression */
          var isAllowed = allowedExtensionsRegx.test(extension);
          if(isAllowed){

          }
          else{
            alert("Invalid file type. Please upload only .csv type file!");
            return false;
          }
        }
      }
