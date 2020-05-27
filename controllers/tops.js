const ensureAuthenticated = require('./config/authenticate');

module.exports = function(app) {

    app.get('/tops', ensureAuthenticated, function(req, res) {
       res.render('tops');
    });
}