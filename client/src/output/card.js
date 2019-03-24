import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Chips from '../chips.js'
import Switches from '../switches.js'


function createData(listData, index) {
  var Case = "Topic"
  var cardType = listData[0];
  var cardValue = listData[1];
  return { index, Case, cardType, cardValue } ;
  }

var cardsData = [
  [
  "Judge",
  "mahajan",]
,
[
  "Act",
  "indian stamp act"]
].map((ele, ind) => createData(ele, ind) );  


class Demo extends Component{
  constructor(...props){
    super(...props);
  this.state = {
    minWidth  : 240,
    color : '',
    fontSize: 14,
    marginBottom: 12,
    padding : 10,
    margin :10,
    cardsColor : ['','']
  }
this.handleToggle = this.handleToggle.bind(this);
}

handleToggle(colorDecider, index){
  var localcardsColor = this.state.cardsColor;
  if(!colorDecider)
   {
       console.log(index);
       localcardsColor[index] = '';
       
   }
   else if(colorDecider) 
  {
    console.log(index);
      localcardsColor[index] = '#e6e6e6';
  }
  this.setState({
    cardsColor : localcardsColor
  })  
}
 
render() {
     return (
          <div id="content" className="flex-container">
            {cardsData.map( ele => (
              <Card  className="card" style={{ color : this.state.cardsColor[ele.index] }} id={ele.index} >
                <div id="case"><h3 href="#"> {ele.Case}</h3><Switches id={ele.index} OnPassChecked={this.handleToggle}  /></div>
                <div id="cardType">
                  <b><h3>{ele.cardType}:</h3></b> 
                </div>
                <div id="cardValue">
                  <b><h3>{ele.cardValue}</h3></b> 
                </div>
                {/* <br /><br />
                <Chips />     */}
               </Card>
            ))}
          </div>
           );
     }
     

    }

    export default Demo;