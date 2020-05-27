const mongoose = require('mongoose');

// schema
var registerschema = new mongoose.Schema({
    firstname: {
        type: String,
        required: true
    },
    lastname: {
        type: String,
        required: true
    },
    institution: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    username : {
        type: String,
        required: true
    },
    password : {
        type: String,
        required: true
    },
    phoneareacode: {
        type: String,
        required: true
    },
    phonenumber: {
        type: Number,
        required: true
    },
    language: {
        type: String,
        required: true
    },
    usertype: {
        type: String,
        required: true
    },
});

const register = mongoose.model('register', registerschema);

module.exports = register