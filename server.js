


var express = require('express')
var app = express();
var router = require('./router/main')(app);
var port = 3000;

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

var server = app.listen(port, function(){
    console.log("express server has started on port", port)
});

app.use(express.static('public'));

/*
    // Router
    app.get('/', function(reg, res){
        res.send('Hello World');
    });

*/





