import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { MDBCol, MDBFormInline, MDBBtn } from "mdbreact";
import MySlider from './slider.js'
import Select from 'react-select';
import acts from './actsfinal.js';

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
      <Container> 
      <Row>
        <Col md={12}><SearchBar OnQueryPass={this.updateResultQuery} /></Col>
      </Row>
      <Row>
        <Col md={12}><MySlider triggeerParent onSliderDataPass={this.updateSliderResult}  /></Col>
        <Col md={6}><Category onCategoryDataPass={this.updateResultCat}  /></Col>
        <Col md={6}><Judges  OnJudgeNamePass={this.updateResultJudge} /></Col>
      </Row>
      <Row>
        <Col><Acts onSeacrchedActsPass={this.updateSearchedResultAct} onSelectedActsPass={this.updateResSelectedAct} /></Col>
      </Row> 
    </Container>
    );
  }
}

const wrapperStyle = {  margin: 20 };

class SearchBar extends Component{
  constructor(props){
    super(props);
    this.passQuery = this.passQuery.bind(this)
  }

  passQuery(event){
    var searchedQuery = event.target.value;
    this.props.OnQueryPass(searchedQuery);

  }
    
  render(){
    return (

      <MDBCol md="12" style={wrapperStyle}>
        <h3> Query </h3>
        <MDBFormInline className="md-form mr-auto mb-4">
          <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" id="query" onChange={this.passQuery} defaultValue='' />
          <MDBBtn gradient="aqua" rounded size="sm" type="submit" className="mr-auto">
          </MDBBtn>
          </MDBFormInline>
      </MDBCol>
    );
  }
}

class Category extends Component{
constructor(props){
  super(props);
  this.passData = this.passData.bind(this); 
}

 passData(event){
   var searchedCat = event.target.value;
   this.props.onCategoryDataPass(searchedCat);
}
 
  render(){
  return (
    <MDBCol md="12" style={wrapperStyle}>
      <h3> Category </h3>
      <MDBFormInline className="md-form mr-auto mb-4">
          <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" id="category" onChange={this.passData} defaultValue = ''  />
      </MDBFormInline>
    </MDBCol>
  );
 }
}

class Judges extends Component{
  constructor(props){
    super(props);
    this.passDataJudges = this.passDataJudges.bind(this);
  }

  passDataJudges(event){
    var searchedJudge = event.target.value;
    this.props.OnJudgeNamePass(searchedJudge);
  }
  
  render(){
    return (
      <MDBCol md="12" style={wrapperStyle}>
        <h3> Judges </h3>

        <MDBFormInline className="md-form mr-auto mb-4">
          <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" id="judge"  onChange={this.passDataJudges} defaultValue = '' />
        </MDBFormInline>
      </MDBCol>
    );
  }
}
 
class Acts extends Component{
  constructor(props){
    super(props);
      this.state = {
        glines : [],
        selectedOptions: []
     };
    this.handleChange = this.handleChange.bind(this);
    this.handleSelection = this.handleSelection.bind(this);
   }
    
 handleChange(event){
   var firstLetter = '';
   if(event[0] === undefined){
     this.setState({
       glines: []
     });
     return;
   }
   if(event[0] === firstLetter) {
     return;
   } else {
     firstLetter = event[0].toLowerCase();
   }
   
   if(firstLetter !== undefined){
     this.setState  ({
       glines : acts.acts[firstLetter]
    })
   } else {
     this.setState({
       glines: []
     });
   }

  var searchedAct = event;
  this.props.onSeacrchedActsPass(searchedAct);
  }

  
  handleSelection = (selectedOptions) => {
       this.props.onSelectedActsPass(selectedOptions);
  }

  render(){
    return (
    <div className="app">
      <div className="container">
        <Select options={this.state.glines}  onInputChange={this.handleChange} onChange={this.handleSelection}  isMulti />
      </div>
    </div>
  );
 }
}

export default App;
