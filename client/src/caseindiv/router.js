import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import JudgeIndiv from './JudgeIndiv.js'
import ActIndiv from './ActIndiv.js'
import App from '../App.js'
import Output from '../output/output.js'
import Modal from './modal.js'

class Router extends Component {
    render() {
      return (
        <BrowserRouter>
            <Switch>
              <Route exact path='/' component={App} />  
              <Route exact path="/judge" component={JudgeIndiv}  />
              <Route exact path="/act/sectionx" component={ActIndiv}  />
              <Route exact path='/output' component={Output} />
              <Route exact path='/modal' component={Modal}  />
            </Switch>
        </BrowserRouter>
      );
    }
  };
  
  export default Router; 