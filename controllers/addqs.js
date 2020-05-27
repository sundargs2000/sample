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
    app.get('/addqs', ensureAuthenticated, 
    function(req, res)
    {
        res.render('addqs');
    }
    );

    app.post
    (
        '/addqs',
        ensureAuthenticated,
        function(req, res)
        {
            problem(req.body)
            .save
            (
                function(err, data)
                {
                    if(err) throw err;
                    res.redirect('qList');
                }
            );
        }
    );
}