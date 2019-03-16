import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import Demo from './output.js';
import Tabler from './table.js';
import Advfilter from './advtable.js';
import VerticalTimeline2 from './verticaltimeline.js';


ReactDOM.render(<App />, document.getElementById('root'));
ReactDOM.render(<Demo />, document.querySelector('#output'));
ReactDOM.render(<Tabler />, document.querySelector('#tabler'));
ReactDOM.render(<Advfilter />, document.querySelector('#adv'));
ReactDOM.render(<VerticalTimeline2 /> ,document.getElementById('vone'));
//eactDOM.render(<Test />,document.getElementById('check'));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
