var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');

var args = process.argv;

var http = require("http");
var fs = require("fs");
var app = http.createServer(function(req, res){

    res.end(fs.readFileSync(__dirname + '/' + args[2]));


})
var port = 3000;
console.log("Http server has started on port", port);
app.listen(port);


// var router = require('./router/main')(app, args);

// var port = 3000;

// var win = window.open("/iPhone.html", "mywindow");


// app.use(express.static('public'));
// //app.set('views', __dirname + '/views');
// app.set('view engine', 'ejs');
// app.engine('html', require('ejs').renderFile);

// var server = app.listen(port, function(){
//     console.log("express server has started on port", port)
// });

// app.use(express.static('iPhone_files'));





