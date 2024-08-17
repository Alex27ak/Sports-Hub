const express = require('express');
const router = express.Router();
const User = require('../models/User');
const Registration = require('../models/Registration');

router.get('/admin', async (req, res) => {
    if (req.user.email !== "preetikanadar05@gmail.com") {
        return res.redirect('/');
    }

    const users = await User.find({});
    const registrations = await Registration.find({}).populate('user');
    res.render('admin', { users, registrations });
});

module.exports = router;
