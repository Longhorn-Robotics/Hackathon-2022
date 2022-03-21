//takes user info from HTML turns it into a JS object and parses it into json (for people registering)
/*
var registrationInfoArray = [];

function getVal() {
    let val = String(document.querySelector('input').value);
    console.log(val);
    object_array.push(val);
}

var registrationInfoObject = {
    Email: object_array[0],
    Password: object_array[1],
    First_Name: object_array[2],
    Last_Name: object_array[3]
}

function sendToRaven(){
    fetch('https://pro-student.herokuapp.com/', {
    method: 'POST', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(registrationInfoObject),
    })
    .then(response => response.json())
    .then(data => {
    console.log('Success:', data);
    })
    .catch((error) => {
    console.error('Error:', error);
    });
}

function check_error(){
    var submitable = True;
    for(var i=0; i < 4; i++){
        if(object_array[i] == null){
            submitable = False;
        }
    }
    if (submitable == True){
        sendToRaven();
    } else{
        alert("Please fill out all required information.");
    }
    registrationInfoArray = [];
}

//takes user info from HTML turns it into a JS object and parses it into json (for people Loging-In)
var registrationInfoObject = {
    Email: object_array[0],
    Password: object_array[1],
}

function check_error(){
    var submitable = True;
    for(var i=0; i < 2; i++){
        if(object_array[i] == null){
            submitable = False;
        }
    }
    if (submitable == True){
        sendToRaven();
    } else{
        alert("Please fill out all required information.");
    }
    registrationInfoArray = [];
}
*/

//takes inputs to manually create assignments
var assignmentData = [];

function getVal() {
    let val = String(document.querySelector('input').value);
    console.log(val);
    assignmentData.push(val);
}

var assignmentInfoObject = {,
    AssignmentName: assignmentData[0],
    DueDate: assignmentData[1],
    WarnDate: assignmentData[2]
}

function sendToRaven(){
    fetch('https://pro-student.herokuapp.com/v1/assignments', {
    method: 'PUT', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(assignmentInfoObject),
    })
    .then(response => response.json())
    .then(data => {
    console.log('Success:', data);
    })
    .catch((error) => {
    console.error('Error:', error);
    });
}

function check_error(){
    var submitable = True;
    for(var i=0; i < 3; i++){
        if(assignmentData[i] == null){
            submitable = False;
        }
    }
    if (submitable == True){
        sendToRaven();
    } else{
        alert("Please fill out all required information.");
    }
    assignmentData = [];
}

//requests json file with the information about the user's assignments from python and gives it to HTML
/*const IdStatus = {
    id: 1
}
*/

fetch('https://pro-student.herokuapp.com/assignments', {
    method: 'GET', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(assignmentList),
    })
    .then(response => fetchedData = response.json())
    .then(data => {
    console.log('Success:', data);
    })
    .catch((error) => {
    console.error('Error:', error);
});

