document.getElementById("upload-form").addEventListener("submit", function (event) {
    event.preventDefault();
    
    const fileInput = document.getElementById("image-upload");
    if (fileInput.files.length === 0) {
        alert("Please select a file before uploading.");
        return;
    }
  
    alert("Image uploaded successfully! Prediction feature coming soon.");
  });