// TODO: Sa fac sa fie pe coloane si pe linii

number_of_cameras= 0;

function myFunction() {
  if(number_of_cameras%2!==0){
      var div = document.createElement('div'); // Create div for CameraArticle element

      var div_title = document.createElement('div'); // Create div for Camera Title which will contain all the elements
      div_title.className= "CameraTitle"; // set div clann name as "CameraTitle"
      div_title.setAttribute = number_of_cameras; // make the title of the camera the ipAddress of that camera

      var input = document.createElement('input'); // Create input element
      input.type = 'checkbox'; // Make the input element as a checkbox
      div_title.appendChild(input); // Append the input the the CameraTitle div

      var video = document.createElement('video'); // Create video
      video.src = 'http://'; // Add the src of the video variable
      video.autoplay = 'true'; // Make the video autoplay
      video.id= 'videoplayer/' + ipAddress; // Make the id of the video as: "videoplayer/" and the actual ipAddress
      div_title.appendChild(video); //  Append the video to the CameraTitle

      div.appendChild(div_title); //  Append the div_title to the main div("CameraArticle")

      number_of_cameras++; // Increment number_of_cameras variable
      document.body.appendChild(div); // Append the main div into the HTML document
    }
    else{



      number_of_cameras++; // Increment number_of_cameras variable
      document.body.appendChild(div); // Append the main div into the HTML document
    }
  }