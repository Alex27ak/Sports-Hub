require('dotenv').config();
const mongoose = require('mongoose');
const express = require('express');
const session = require('express-session');
const passport = require('passport');
const User = require('./models/User');
const authRoutes = require('./routes/auth');
const app = express();

const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI; // Ensure this is correctly set in your .env file

mongoose.connect(MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Connected to MongoDB');
}).catch((err) => {
  console.error('Failed to connect to MongoDB', err);
});

app.use(express.urlencoded({ extended: false }));
app.use(session({
  secret: 'yourSecret',
  resave: false,
  saveUninitialized: false,
}));

app.use(passport.initialize());
app.use(passport.session());

app.use(express.static('public'));
app.use(authRoutes);

app.set('view engine', 'ejs');

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
