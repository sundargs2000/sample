const ensureAuthenticated = require('./config/authenticate');
const nodemailer = require("nodemailer");
var mongoose = require('mongoose');

// connect to db
mongoose.connect('mongodb+srv://nativlang:donkeymonkey@nativlang-u2azm.mongodb.net/test?retryWrites=true&w=majority', {
    useNewUrlParser: true,
});


var register = require('./config/auth');


module.exports = function(app) {

    app.get
    (
        '/thint', 
        ensureAuthenticated, 
        function(req, res) 
        {
            res.render('thint');
        }
    );

    app.post
    (
        '/thint',
        function(req, res)
        {
            register.find
            ( 
                {},
            )
            .then
            (
                function(tit)
                {
                    var maillist = '';
                    for(i=0; i<tit.length; i++)
                    {
                        maillist = maillist +','+ tit[i]['email'];
                    }
                    console.log(maillist);
                    let transporter = nodemailer.createTransport({
                        host: "smtp.gmail.com",
                        // port: 587,
                        // secure: false, // true for 465, false for other ports
                        auth: {
                            user: 'jaisriram2024@gmail.com', // generated ethereal user
                            pass: 'ramramram' // generated ethereal password
                        }
                        });

                    let mailOptions = {
                        from: 'jaisriram2024@gmail.com', // sender address
                        to: maillist, // list of receivers
                        subject: "Hint", // Subject line
                        text: req.body.title.toString('utf-8')+'\n'+req.body.hint.toString('utf-8'), // plain text body
                    }
        
                    transporter.sendMail
                    (
                        mailOptions,
                        function(err, data)
                        {
                            if(err)
                            {
                                console.log(err);
                                res.send(err);
                            }
                            else
                            {
                                console.log('Email sent', data);
                                res.render('tops');
                            }
                        } 
                    );
                }
            )
        }
    )
}