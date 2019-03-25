import React, { Component } from 'react';
import Select from 'react-select';
import acts from './actsfinal.js';
 
var i = -1;
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
  
    }
  
    
    handleSelection = (selectedOptions) => {
      
        this.props.onSelectedActsPass(selectedOptions);
    }

    
    render(){
      const trimLongActs = (data) =>{
        if(data.label.length > 135){
          return(
            data.label = data.label.slice(0,135) + '...'
          )
        }
        else{
          return data.label;
        }
        
      }
      return (
      <div className="app">
        <div className="container">
          <Select 
          options={this.state.glines}  
          onInputChange={this.handleChange} 
          onChange={this.handleSelection}   
          isMulti 
          formatOptionLabel={trimLongActs}
          />
        </div>
      </div>
    );
   }
  }

  export default Acts;