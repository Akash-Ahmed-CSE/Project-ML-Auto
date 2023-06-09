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
        console.log("input element", inputElement.files);
        var files = inputElement.files;
        if(files.length==0){
          alert("Please choose a file first...");
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
           // alert("File type is valid for the upload!");
            /*file upload logic goes here... */


           /* const form = document.getElementById('file-input');
            console.log("form", form);
            let file = form.files[0]
              let formData = new FormData();
              formData.set('file', file);
              console.log('formData',formData);
              // convert the form into POST data
              const serializedFormData = new FormData(event.target);
              console.log("serializedFormData", serializedFormData);
              // use your favorite AJAX library
              axios.post(
                "D:/Projects/ML Projects/CKD Implementation(ML based web project)/data",
                serializedFormData
              ).then(response => {
                console.log("success!");
                console.log("");
              }).catch(error => {
                console.log("falied!");
                console.log(error.response);
              });



              // fetch('../data/' + encodeURIComponent(filename), {method:'PUT',body:fileInput.files[0]});
              // console.log("formData", fileInput.files[0]);


  /*const formData = new FormData(form);

  const fetchOptions = {
    method: form.method,
    body: formData,
  };

  fetch(url, fetchOptions);

    alert('The file has been uploaded successfully.');*/
          }
          else{
            alert("Invalid file type. Please upload only .csv type file!");
            return false;
          }
        }
      }
