var mongoose = require('mongoose');
var bodyParser = require('body-parser'); 

// connect to db
mongoose.connect('mongodb+srv://nativlang:donkeymonkey@nativlang-u2azm.mongodb.net/test?retryWrites=true&w=majority', {
    useNewUrlParser: true
});

var register = require('./config/auth');

module.exports = function(app) 
{

    app.get('/register', 
    function(req, res) 
    {
       res.render('register');
    }
    );

    app.post('/register', 
    function (req, res) 
    {
        
        let errors = [];
        temp = register(req.body);

        if(!temp['usertype'] || !temp['language'])
        {
            errors.push({msg: 'Please select User Type and Language'});
            console.log(errors);
            res.render('register', 
            {
                errors,
                firstname: temp['firstname'],
                lastname: temp['lastname'],
                institution: temp['institution'],
                email: temp['email'],
                username: temp['username'],
                password: temp['password'],
                phoneareacode: temp['phoneareacode'],
                phonenumber: temp['phonenumber']
            }
            );
        }
        else {
        register.exists({ email: temp['email'] })
        .then(
            function(lol)
            {
                if(lol) 
                {
                    errors.push({msg: 'email exists'});
                    console.log(errors);
                    res.render('register', 
                    {
                        errors,
                        firstname: temp['firstname'],
                        lastname: temp['lastname'],
                        institution: temp['institution'],
                        email: temp['email'],
                        username: temp['username'],
                        password: temp['password'],
                        phoneareacode: temp['phoneareacode'],
                        phonenumber: temp['phonenumber']
                    }
                    );
                }
                else 
                {
                    register.exists({ username: temp['username'] })
                    .then(
                        function(lol1)
                        {
                            if(lol1)
                            {
                                errors.push({msg: 'this username exists'});
                                console.log(errors);
                                res.render('register', 
                                {
                                    errors,
                                    firstname: temp['firstname'],
                                    lastname: temp['lastname'],
                                    institution: temp['institution'],
                                    email: temp['email'],
                                    username: temp['username'],
                                    password: temp['password'],
                                    phoneareacode: temp['phoneareacode'],
                                    phonenumber: temp['phonenumber']
                                }
                                );
                            }
                            else
                            {
                                temp.save(
                                    function (err, data) 
                                    {
                                        if (err) throw err;
                                        res.render('login');
                                    });  
                            }
                        }
                    );
                }
            }
        );
        }
    });
}


      