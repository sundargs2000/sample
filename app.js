var express = require('express');
var passport = require('passport');
var app = express();
const session = require('express-session');
var mongoose = require('mongoose');

//local strategy
var register = require('./controllers/config/auth');
var LocalStrategy = require('passport-local').Strategy;

//controllers
var qList = require('./controllers/qList');
var login = require('./controllers/login');
var register1 = require('./controllers/register');
var logout = require('./controllers/logout');
var addqs = require('./controllers/addqs');
var ide = require('./controllers/ide');
var solve = require('./controllers/solve');
var tlogin = require('./controllers/tlogin');
var tops = require('./controllers/tops');
var thint = require('./controllers/thint');

//passport config
passport.use(new LocalStrategy(
  function(username, password, done) {
    register.findOne({ username: username }, function (err, user) {
      if (err) { return done(err); }
      if (!user) { return done(null, false); }
      // console.log(user.password,password);
      if (user.password!==password) { return done(null, false); }
      return done(null, user);
    });
  }
));

//template engine
app.set('view engine', 'ejs');

// Express body parser
app.use(express.urlencoded({ extended: true }));

// Express session
app.use(
    session({
      secret: 'secret',
      resave: true,
      saveUninitialized: true
    })
  );

//passport midware
app.use(passport.initialize());
app.use(passport.session());

//static files
app.use(express.static('./public'));

//middleware
app.use(express.urlencoded({extended: false}));



//listen port
app.listen(8888);
console.log('listening to 8888');

//fire
register1(app);
login(app);
tlogin(app);
qList(app);
tops(app);
logout(app);
addqs(app);
thint(app);
ide(app);
solve(app);
