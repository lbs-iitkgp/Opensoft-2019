import dotenv from 'dotenv'
import db from 'db'
//require('dotenv').config
//dotenv.config()
// const db = require('db')

db.connect({
  host: process.env.DB_HOST,
  username: process.env.DB_USER,
  password: process.env.DB_PASS
})

const result = dotenv.config()
 
if (result.error) {
  throw result.error
}
 
console.log(result.parsed)
require('dotenv').config({ path: '/full/custom/path/to/your/env/vars' })

const dotenv = require('dotenv')
const buf = Buffer.from('BASIC=basic')
const config = dotenv.parse(buf) // will return an object
console.log(typeof config, config) // object { BASIC : 'basic' }


