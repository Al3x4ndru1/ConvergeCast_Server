number_of_cameras_selected = 0;


function myFunction() {
    if (number_of_cameras_selected==0){
        alert("Please select a camera");
    }else{
        console.log("Is checked");
    }

    
}



function selectCameras(cb){
    if(document.getElementById(cb).checked){
        number_of_cameras_selected++;
    }
    else{
        number_of_cameras_selected--;
    }

}