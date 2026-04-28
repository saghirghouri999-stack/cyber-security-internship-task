const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const validator = require('validator');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const helmet = require('helmet');
const winston = require('winston');

const app = express();
const PORT = 3000;
const SECRET_KEY = 'your-secret-key';

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public'));
app.use(helmet());

const logger = winston.createLogger({
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'security.log' })
  ]
});

let users = [];

function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) return res.status(401).send('Access denied');

  jwt.verify(token, SECRET_KEY, (err, user) => {
    if (err) return res.status(403).send('Invalid token');
    req.user = user;
    next();
  });
}

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'signup.html'));
});

app.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'login.html'));
});

app.get('/profile', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'profile.html'));
});

app.get('/profile-data', authenticateToken, (req, res) => {
  res.send({
    message: 'Protected profile data',
    user: req.user
  });
});

app.post('/signup', async (req, res) => {
  const { name, email, password } = req.body;
  logger.info(`Signup attempt for email: ${email}`);

  if (!name || !email || !password) {
    return res.status(400).send('All fields are required');
  }

  if (!validator.isEmail(email)) {
    return res.status(400).send('Invalid email format');
  }

  if (!validator.isLength(password, { min: 6 })) {
    return res.status(400).send('Password must be at least 6 characters long');
  }

  const existingUser = users.find(u => u.email === email);
  if (existingUser) {
    return res.status(400).send('User already exists');
  }

  const safeName = validator.escape(name);
  const hashedPassword = await bcrypt.hash(password, 10);

  users.push({ name: safeName, email, password: hashedPassword });

  logger.info(`User registered successfully: ${email}`);
  res.send(`User registered successfully: ${safeName}`);
});

app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  logger.info(`Login attempt for email: ${email}`);

  const user = users.find(u => u.email === email);

  if (!user) {
    logger.warn(`Login failed for email: ${email}`);
    return res.status(401).send('Invalid credentials');
  }

  const isMatch = await bcrypt.compare(password, user.password);

  if (!isMatch) {
    logger.warn(`Login failed for email: ${email}`);
    return res.status(401).send('Invalid credentials');
  }

  const token = jwt.sign(
    { email: user.email, name: user.name },
    SECRET_KEY,
    { expiresIn: '1h' }
  );

  logger.info(`Login successful for email: ${email}`);
  res.send({ message: 'Login successful', token });
});

app.listen(PORT, () => {
  logger.info(`Application started on http://localhost:${PORT}`);
  console.log(`App running on http://localhost:3000`);
});