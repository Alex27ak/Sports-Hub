const express = require('express');
const passport = require('passport');
const User = require('../models/User');

const router = express.Router();

// Registration
router.get('/register', (req, res) => {
  res.render('register');
});

router.post('/register', async (req, res) => {
  try {
    const user = new User({ username: req.body.username });
    await User.register(user, req.body.password);
    res.redirect('/login');
  } catch (err) {
    res.redirect('/register');
  }
});

// Login
router.get('/login', (req, res) => {
  res.render('login');
});

router.post('/login', passport.authenticate('local', {
  successRedirect: '/events',
  failureRedirect: '/login',
}));

// Logout
router.get('/logout', (req, res) => {
  req.logout();
  res.redirect('/');
});

module.exports = router;
