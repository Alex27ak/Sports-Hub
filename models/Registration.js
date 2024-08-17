const mongoose = require('mongoose');

const registrationSchema = new mongoose.Schema({
    game: String,
    location: String,
    teamName: String,
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User'
    },
    registeredAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Registration', registrationSchema);
