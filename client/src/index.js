import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import Router from './caseindiv/router.js'

import dotenv from 'dotenv';
dotenv.config({ path: '../' });
console.log(process.env.REACT_APP_BACKEND_ORIGIN);

ReactDOM.render(<Router />,document.getElementById('router'));

//ReactDOM.render(<Test />,document.getElementById('check'));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
