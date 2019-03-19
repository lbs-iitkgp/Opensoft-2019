import React, { Component } from 'react';
import './App.css';
import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';
// import Col from 'react-bootstrap/Col';
//import { MDBCol, MDBFormInline, MDBBtn } from "mdbreact";
import MySlider from './components/slider.js'
//import Select from 'react-select';
//import acts from './components/actsfinal.js/index.js';
// import PropTypes from "prop-types";
// import classNames from "classnames";
// import { withStyles } from "@material-ui/core/styles";
// import MenuItem from "@material-ui/core/MenuItem";
// import TextField from "@material-ui/core/TextField"
import SearchBar from './components/query.js';
import Category from './components/category.js';
import Judges from './components/judges.js';
import Acts from './components/acts.js'

class App extends Component {
 constructor(props){
   super(props);
  
  this.updateResultCat = this.updateResultCat.bind(this);
  this.updateSearchedResultAct = this.updateSearchedResultAct.bind(this);
  this.updateResultQuery = this.updateResultQuery.bind(this);
  this.updateResultJudge = this.updateResultJudge.bind(this);
  this.updateResSelectedAct = this.updateResSelectedAct.bind(this);
  this.updateSliderResult = this.updateSliderResult.bind(this);
}


updateSearchedResultAct(searchedActPass){
   console.log(searchedActPass);
}

updateResultJudge(JudgeRes){
   console.log(JudgeRes);
}

updateResultCat(catRes){
  console.log(catRes);
}
 
updateResultAct(joinedActs){
  console.log(joinedActs);
}

updateResultQuery(queryRes){
  console.log(queryRes);
}

updateResSelectedAct(selectedActPass){
  console.log(selectedActPass);
}

updateSliderResult(sliderPass){
  console.log(sliderPass[0], sliderPass[1]);
}
  render() {
    return (
      <Container id='box_shadow'> 
        <h3>Search</h3>
        <SearchBar OnQueryPass={this.updateResultQuery}   />
        <MySlider onSliderDataPass={this.updateSliderResult}  />
        <Category onCategoryDataPass={this.updateResultCat}  />
        <Judges  onJudgeNamePass={this.updateResultJudge} /> 
        <br />
        <h3>Acts</h3>
        <Acts onSeacrchedActsPass={this.updateSearchedResultAct} onSelectedActsPass={this.updateResSelectedAct} />
     </Container>
    );
  }
}



export default App;
