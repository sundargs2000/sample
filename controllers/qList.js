const ensureAuthenticated = require('./config/authenticate');
var mongoose = require('mongoose');

// connect to db
mongoose.connect('mongodb+srv://nativlang:donkeymonkey@nativlang-u2azm.mongodb.net/test?retryWrites=true&w=majority', {
    useNewUrlParser: true
});

//getting schema
var problem = require('./config/qs');

module.exports = function(app) {

    app.get
    (
        '/qList', 
        ensureAuthenticated, 
        function(req, res) 
        {
            problem.find
            ( 
                {},
            )
            .then
            (
                function(tit)
                {
                    var data = [];
                    var id = [];
                    for(i=0; i<tit.length; i++)
                    {
                        data.push(tit[i]['title']);
                        id.push(tit[i]['_id'])
                    }
                    res.render('qList', {qs: data, id: id}); 
                }
            )
        }
    );

    app.post
    (
        '/qList',
        function(req, res)
        {
            // console.log(req.body['qid']);
            problem.findOne
            (
                { '_id': req.body['qid'] } 
            )
            .then
            (
                function(lol)
                {
                    res.render
                    (
                        'solve', 
                        { 
                            data: problem(lol),
                            solution: '',
                            stusol: [],
                            realsol: [] 
                        }
                    );
                }
            )
        }
    )
}