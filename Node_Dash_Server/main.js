//ac:63:be:e7:7e:75
//warning this may trigger multiple times for one press
//...usually triggers twice based on testing for each press
var dash_button = require('node-dash-button');
var status=0;
var request = require('request');
var dash = dash_button("ac:63:be:e7:7e:75", null, 60000, 'all'); //address from step above
dash.on("detected", function (){
    if(status==0){
        status=1;
        request.post(

        {
            url:'http://192.168.1.16:5000/all',
            headers:{
            "Content-Type": "application/json"
            },
            json:{"on":true, "bri": 255}
        }
        );
    }
    else{
        status=0;
        request.post(

        {
            url:"http://192.168.1.16:5000/all",
            headers:{
            "Content-Type": "application/json"
            },
            json:{"on":false}
        }
        );
    }
    //console.log("fatto");
});