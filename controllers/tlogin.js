var mongoose = require('mongoose');
var passport = require('passport');

// connect to db
mongoose.connect('mongodb+srv://nativlang:donkeymonkey@nativlang-u2azm.mongodb.net/test?retryWrites=true&w=majority', {
    useNewUrlParser: true,
});

var register = require('./config/auth');

module.exports = function(app) {

    app.get('/tlogin', function(req, res) {
       res.render('tlogin');
    });

    app.post
    (
        '/tlogin',
        function(req, res, next)
        {
            register.findOne
            (
                {username: req.body.username },
                function(err, user)
                {
                    if (err) { res.render('tlogin'); }
                    if (!user) { res.render('tlogin'); }
                    if(user.usertype!='Teacher')
                    {
                        res.render('tlogin');
                    }
                    else
                    {
                        passport.authenticate
                        (
                            'local',
                            {
                                successRedirect: '/tops',
                                failureRedirect: '/tlogin',
                                failureFlash: true
                            }
                        )
                        (req, res, next);
                        
                        passport.serializeUser(function(user, done) {
                            done(null, user.id);
                        });
                        
                        passport.deserializeUser(function(id, done) {
                            register.findById(id, function(err, user) {
                            done(err, user);
                            })
                        });
                    }
                } 
            )
            
        } 
    );
}