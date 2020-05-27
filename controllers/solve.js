const ensureAuthenticated = require('./config/authenticate');
var mongoose = require('mongoose');

// connect to db
mongoose.connect('mongodb+srv://nativlang:donkeymonkey@nativlang-u2azm.mongodb.net/test?retryWrites=true&w=majority', {
    useNewUrlParser: true
});

//getting schema
var problem = require('./config/qs');

module.exports = function(app)
{
    app.post
    (
        '/solve',
        function(req, res)
        {
            // console.log(req.body);
            // console.log('running')
            // var spawn = require('child_process').spawn;
            // var process = spawn('python', [ './controllers/temp.py', req.body.solution.toString('utf-8') ]);
            // process.stderr.on('data', function(data){
            //     res.send(data.toString('utf-8'));
            // });
            // process.stdout.on('data', function(data){
            //     problem.findOne
            //     (
            //         { '_id': req.body.id } 
            //     )
            //     .then
            //     (
            //         function(lol)
            //         {
            //             dat1 = req.body.solution.toString('utf-8');
            //             res.render
            //             (
            //                 'solve', 
            //                 { 
            //                     data: problem(lol),
            //                     solution: dat1,
            //                     stusol: [ data ],
            //                     realsol: [ problem(lol)['solution'] ]   
            //                 }
            //             );
            //         }
            //     )
            // });

            var spawn = require('child_process').spawnSync;
            var processo = spawn('python', [ './controllers/temp1.py', req.body.solution.toString('utf-8') ]);
            
            console.log(processo.stdout.toString())
            console.log(processo.stderr.toString())

            problem.findOne
            (
                { '_id': req.body.id } 
            )
            .then
            (
                function(lol)
                {
                    dat1 = req.body.solution.toString('utf-8');
                    res.render
                    (
                        'solve', 
                        { 
                            data: problem(lol),
                            solution: dat1,
                            stusol: [ processo.stdout ],
                            realsol: [ problem(lol)['solution'] ]   
                        }
                    );
                }
            );

            // var process = require('child_process').execSync
            // (
            //     'python ' + './controllers/temp1.py ' + req.body.solution.toString('utf-8'),
            //     function(err, stdout, stderr)
            //     {
            //         if(err)
            //         {
            //             console.log(err);   
            //         }

            //         if(stderr)
            //         {
            //             problem.findOne
            //             (
            //                 { '_id': req.body.id } 
            //             )
            //             .then
            //             (
            //                 function(lol)
            //                 {
            //                     dat1 = req.body.solution.toString('utf-8');
            //                     res.render
            //                     (
            //                         'solve', 
            //                         { 
            //                             data: problem(lol),
            //                             solution: dat1,
            //                             stusol: [ stderr ],
            //                             realsol: [ problem(lol)['solution'] ]   
            //                         }
            //                     );
            //                 }
            //             )   
            //         }

            //         problem.findOne
            //         (
            //             { '_id': req.body.id } 
            //         )
            //         .then
            //         (
            //             function(lol)
            //             {
            //                 dat1 = req.body.solution.toString('utf-8');
            //                 res.render
            //                 (
            //                     'solve', 
            //                     { 
            //                         data: problem(lol),
            //                         solution: dat1,
            //                         stusol: [ stdout ],
            //                         realsol: [ problem(lol)['solution'] ]   
            //                     }
            //                 );
            //             }
            //         )
            //     }
            // );
            
        }
    );
}