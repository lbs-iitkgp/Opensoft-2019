import React, { Component } from 'react';
import './App.css';
import Container from 'react-bootstrap/Container';
import MySlider from './components/slider.js'
import SearchBar from './components/query.js';
import Category from './components/category.js';
import Judges from './components/judges.js';
import Acts from './components/acts.js'
import Navbar from './navbar.js'
import Button from '@material-ui/core/Button';

var Results={
  query : '',
  years : [],
  category : '',
  judgeName : '',
  selectedActs :[]
}
class App extends Component {
 constructor(props){
   super(props);
  
  this.updateResultCat = this.updateResultCat.bind(this);
  this.updateResultQuery = this.updateResultQuery.bind(this);
  this.updateResultJudge = this.updateResultJudge.bind(this);
  this.updateResSelectedAct = this.updateResSelectedAct.bind(this);
  this.updateSliderResult = this.updateSliderResult.bind(this);
}



updateResultJudge(JudgeRes){
  Results.judgeName = JudgeRes; 
}

updateResultCat(catRes){
  Results.category = catRes;
}
 
updateResultQuery(queryRes){
  Results.query=queryRes
  }

updateResSelectedAct(selectedActPass){
  Results.selectedActs = selectedActPass
}

updateSliderResult(sliderPass){
  Results.years  = sliderPass.slice(0,2)
  }

printResults(){
  console.log(Results.query);
  console.log(Results.years[0], Results.years[1]);
  console.log(Results.category);
  console.log(Results.judgeName);
  console.log(Results.selectedActs);

}
  render() {
    return (
      <div>
      <Navbar />  
      <br></br>
      <Container id='box_shadow'> 
        <h3>Search</h3>
        <SearchBar OnQueryPass={this.updateResultQuery}   />
        <MySlider onSliderDataPass={this.updateSliderResult}  />
        <Category onCategoryDataPass={this.updateResultCat}  />
        <Judges  onJudgeNamePass={this.updateResultJudge} /> 
        <br />
        <h3>Acts</h3>
        <Acts  onSelectedActsPass={this.updateResSelectedAct} />
        <br />
        <div className='searchButton'>
            <Button variant="contained" color="primary" onClick={this.printResults}>
                Search
            </Button>
        </div>
     </Container>
     </div>
    );
  }
}



export default App;
