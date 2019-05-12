var http = require('http').createServer().listen(4000);
var io = require('socket.io')(http);
var XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;

const fs = require('fs')

var express = require('express')

var app = express()
app.use(express.static("public"));
app.listen(4001)

//function
function randomstring(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
 }

app.get("/",function(req, res) {
    res.redirect('/')
})
// creating an instance of XMLHttpRequest
var xhttp = new XMLHttpRequest();

// host of the server
var host = 'localhost';
var port = '8000';

// when a connection happens (client enters on the website)
io.on('connection', function(socket) {

    // if the event with the name 'message' comes from the client with the argument 'msgObject',
    // which is an object with the format: {'user_name': < name >, 'message': < message >},
    // it emits for every connected client that a message has been sent, sending the message to the event
    // 'getMessage' in the client side
    socket.on('message', function(msgObject) {  
        // emits the msgObject to the client
        io.emit('getMessage', msgObject);

        // url of the view that will process
        var url = 'http://' + host +':' + port + '/save_message/';

        // when the request finishes
        xhttp.onreadystatechange = function() {
            // it checks if the request was succeeded
            if(this.readyState === 4 && this.status === 200) {
                // if the value returned from the view is error
                if(xhttp.responseText === "error")
                    console.log("error saving message");
                // if the value returned from the view is success
                else if(xhttp.responseText === "success")
                    console.log("the message was posted successfully");
            }
        };

        // prepares to send
        xhttp.open('POST', url, true);
        // sends the data to the view
        xhttp.send(JSON.stringify(msgObject));
    });
    socket.on("client-send-image",function(data){
        var extension=data.oldimgname.split('.').pop();
        var newimgname=randomstring(10)+"."+extension;
        const prefix=__dirname+'/public';
        const path='/upload/'+newimgname;
        fs.writeFileSync(prefix+path,data.img);
        console.log(data.img.toString('base64'));
        io.sockets.emit("server-send-img",{name:data.nameuser,img:data.img.toString('base64')})
    })

});