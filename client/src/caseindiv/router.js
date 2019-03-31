import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import JudgeIndiv from './JudgeIndiv.js'
import ActIndiv from './actsindiv.js'
import App from '../App.js'
import Output from '../output/output.js'
import Modal from './modal.js'
import BasicSearch from '../components/basicSearch.js'
import BasicOutput from '../output/basicOutput.js'
import KeyWords from './keyWords.js'
import CatchyWords from './catchyWords.js'
import YearsIndiv from './yearsindiv.js'
import dotenv from 'dotenv';
import axios from 'axios'


class Router extends Component {
    render() {
      // tried this interpolation,but couldn't succeed,babel added in  the dependencies
     // <Route exact path=`/act/:${num}/:${num1}` component={ActIndiv}  />      

      dotenv.config({path: '../.env'});
      console.log(process.env.BACKEND_ORIGIN);

      return (
        <div>
        <BrowserRouter>
            <Switch>
              <div className="App">
              <Route exact path='/' component={App} />
              <Route exact path='/advSearch/:id' component={App} />
              <Route exact path='/basic' component={BasicSearch} />
              <Route exact path='/basic/output/:id' component={BasicOutput} />
              <Route exact path="/judge/:id" component={JudgeIndiv}  />
              <Route exact path="/act/:id" component={ActIndiv}  />
              <Route exact path='/output' component={Output} />
              <Route exact path='/modal/:id' component={Modal}  />
              <Route exact path='/keywords/:id' component={KeyWords} />
              <Route exact path='/catchwords/:id' component={CatchyWords} />
              <Route exact path='/year/:id' component={YearsIndiv} />
              </div>
            </Switch>
        </BrowserRouter>
        </div>
      );
    }
  }; 
  
  export default Router; 