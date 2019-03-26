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

class Router extends Component {
  num = 2;
  num1=3;
  

  
  render() {
      // tried this interpolation,but couldn't succeed,babel added in  the dependencies
     // <Route exact path=`/act/:${num}/:${num1}` component={ActIndiv}  />      
      return (
        <div>
        <BrowserRouter>
            <Switch>
              <div className="App">
              <Route exact path='/' component={App} />  
              <Route exact path='/basic' component={BasicSearch} />
              <Route exact path='/basic/output' component={BasicOutput} />
              <Route exact path="/judge" component={JudgeIndiv}  />
              <Route exact path="/act" component={ActIndiv}  />
              <Route  exact path='/output' component={Output} />
              <Route exact path='/modal' component={Modal}  />
              <Route exact path='/keyWords' component={KeyWords} />
              <Route exact path='/catchyWords' component={CatchyWords} />
              <Route exact path='/years' component={YearsIndiv} />
              </div>
            </Switch>
        </BrowserRouter>
        </div>
      );
    }
  };
  
  export default Router; 