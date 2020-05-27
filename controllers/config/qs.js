const mongoose = require('mongoose');

// schema
var problemschema = new mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    subdomain: {
        type: String,
        required: true
    },
    score: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    solution : {
        type: String,
        required: true
    },
    tc : {
        type: String,
        required: false
    },
    to: {
        type: String,
        required: false
    },
    difficulty: {
        type: String,
        required: true
    },
});

const problem = mongoose.model('problem', problemschema);

module.exports = problem