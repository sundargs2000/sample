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


// start of prom-client
const client = require('prom-client');
const collectDefaultMetrics = client.collectDefaultMetrics;
// Probe every 5th second.
collectDefaultMetrics({ timeout: 5000 });

const counter = new client.Counter({
  name: 'node_request_operations_total',
  help: 'The total number of processed requests'
});

const histogram = new client.Histogram({
  name: 'node_request_duration_seconds',
  help: 'Histogram for the duration in seconds.',
  buckets: [1, 2, 5, 6, 10]
});

app.get('/', (req, res) => {

  //Simulate a sleep
  var start = new Date()
  var simulateTime = 1000

  setTimeout(function(argument) {
    // execution time simulated with setTimeout function
    var end = new Date() - start
    histogram.observe(end / 1000); //convert to seconds
  }, simulateTime)

  counter.inc();
  
  res.send('Hello world not\n');
});

// Metrics endpoint
app.get('/metrics', (req, res) => {
  res.set('Content-Type', client.register.contentType)
  res.end(client.register.metrics())
})

// end of prom-client

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
