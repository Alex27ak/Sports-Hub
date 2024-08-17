const express = require('express');
const router = express.Router();

// Events Page
router.get('/', (req, res) => {
  res.render('events');
});

// Registration for an Event
router.post('/register', (req, res) => {
  if (!req.isAuthenticated()) {
    return res.redirect('/login');
  }
  // Register for the event logic
  res.redirect('/events');
});

module.exports = router;
