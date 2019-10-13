var express = require('express')
var app = express();
var bodyParser = require('body-parser')
var session = require('express-session')
var fs = require("fs")

var args = process.argv;
var router = require('./router/main')(app, args);

var port = 3000;

app.use(express.static('public'));
//app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);


var server = app.listen(port, function(){
    console.log("express server has started on port", port)
});

app.use(express.static('.'));

/*
    // Router
    app.get('/', function(reg, res){
        res.send('Hello World');
    });

*/





