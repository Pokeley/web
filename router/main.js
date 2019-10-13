
// to be able to be called by another js ('server.js')
module.exports = function(app, args)
{
     app.get('/',function(req,res){
        if (args[2] == "--help"){
            console.log("Usage: node server.js [HTML file] [JSON file]");
        }
        else if (/.html$/.exec(args[2])) {
            var fs = require('fs');
            var _html = fs.readFileSync('C:/Users/김승일/Desktop/CodeWS/cite202/'+ args[2]);
            // var json = JSON.parse(fs.readFileSync('C:/Users/김승일/Desktop/CodeWS/cite202/'+args[3]));
            // console.log("\n\n\n\n\n", args[2], "\n\n\n\n\n");
            //res.send(_html);
            res.render('C:/Users/김승일/Desktop/CodeWS/cite202/'+ args[2]);
        }
        else{
            console.log("To check usage, type 'node server.js --help'");
            res.render('index.html');
        }
     });

     // app.get('/iPhone_files/:filename', function(req,res){
     //    res.send(req.params.filename);

     // });




    app.get('/about',function(req,res){
        res.render('about.html');
    });
}
