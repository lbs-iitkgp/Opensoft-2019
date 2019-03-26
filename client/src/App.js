import React, { Component } from 'react';
import './App.css';
import Container from 'react-bootstrap/Container';
import YearsSlider from './components/slider.js'
import SearchBar from './components/query.js';
import Category from './components/category.js';
import Judges from './components/judges.js';
import Acts from './components/acts.js'
import Navbar from './navbar.js'
import Button from '@material-ui/core/Button';
import ReactDOM from 'react-dom';
import Output from './output/output.js'

var Results = {
  "query" : "",
  "years" : [],
  "category" : "",
  "judgeName" : "",
  "selectedActs" :[]
};  

 class App extends Component {
 constructor(props){
   super(props);
  
  this.updateResultCat = this.updateResultCat.bind(this);
  this.updateResultQuery = this.updateResultQuery.bind(this);
  this.updateResultJudge = this.updateResultJudge.bind(this);
  this.updateResSelectedAct = this.updateResSelectedAct.bind(this);
  this.updateSliderResult = this.updateSliderResult.bind(this);
  this.printResults = this.printResults.bind(this);
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
  //this.props.history.push("/output");
  // this.props.history.push({
  //   pathname : "/output" ,
  //   state : {
  //     defaultAdvSearch : Results.query,
  //     defaultYrs : Results.years,
  //     defaultCategory : Results.category,
  //     defaultJudge : Results.judgeName,
  //     defaultActs : Results.selectedActs
  //   }
  // })
    ReactDOM.render(<Output />,document.getElementById('root'))
    // scrollToComponent(this.refs.OutRef,{align:'bottom'});
    window.scroll({top: 800, left: 0, behavior: 'smooth' })
  }
  render() {
    return (
      <div>
      <Navbar />  
      <br></br>
      <Container id='box_shadow'> 
        <h2>Search</h2>
        <SearchBar OnQueryPass={this.updateResultQuery}   />
        <h2>Years</h2>
        <br />
        <YearsSlider onSliderDataPass={this.updateSliderResult}  />
        <Category onCategoryDataPass={this.updateResultCat}  />
        <Judges  onJudgeNamePass={this.updateResultJudge} /> 
        <br />
        <h2>Acts</h2>
        <Acts  onSelectedActsPass={this.updateResSelectedAct} />
        <br />
        <div className='searchButton'>
            <Button variant="contained" color="primary" onClick={this.printResults} style={{width:'130px',height:'50px'}}>
                Search
            </Button>
        </div>
     </Container>
     </div>
    );
  }
}



export default App;
