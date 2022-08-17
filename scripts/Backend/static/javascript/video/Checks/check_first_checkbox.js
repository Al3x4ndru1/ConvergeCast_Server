

export function ShowImageJavaScript(){
    if(document.getElementById("IpAddress").checked==true){ // check that checkbox with that ipAddress
    return 1; //return 1 if the checkbox is selected
        }
    else{
        return 2; //return 2 if the checkbox is not selected
    }
}