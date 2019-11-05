
// to be able to be called by another js ('server.js')
module.exports = function(app, args)
{
     app.get('/',function(req,res){
        if (/.html$/.exec(args[2])) {
            res.render(args[2]);
        }
        else{
            console.log("Please check usage...");
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
