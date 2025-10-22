const dotenv = require('dotenv');
const path = require('path');

// Explicitly specify the .env file path
dotenv.config({ path: path.resolve(__dirname, '.env') });

console.log(process.env.MONGO_URI);
