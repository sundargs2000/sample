var mongoose = require('mongoose');
var passport = require('passport');

// connect to db
mongoose.connect('mongodb+srv://nativlang:donkeymonkey@nativlang-u2azm.mongodb.net/test?retryWrites=true&w=majority', {
    useNewUrlParser: true,
});


var register = require('./config/auth');



// schema
var userloginschema = new mongoose.Schema({
    username : String,
    password : String,
});

var login = mongoose.model('login', userloginschema);

module.exports = function(app) {

    app.get('/login', function(req, res) {
       res.render('login');
    });

    app.post
    (
        '/login',
        function(req, res, next)
        {
            passport.authenticate
            (
                'local',
                {
                    successRedirect: '/qList',
                    failureRedirect: '/login',
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
    );
}