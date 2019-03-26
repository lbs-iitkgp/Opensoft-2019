import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Switches from '../switches.js'
import Chips from '../chips.js'


function createData(listData, index) {
  var keyWord = listData[0]
  var cardType = listData[1]
  var cardValue = listData[2]
  return { index, keyWord, cardType, cardValue } ;
  }

var cardsData = [
  ['honorable',
  "Judge",
  "mahajan",]
,
['stamp issue',
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
      localcardsColor[index] = '#c6c6c6';
  }
  this.setState({
    cardsColor : localcardsColor
  })  
}
 
render() {
     return (
          <div id="content" className="flex-container">
            {cardsData.map( ele => (
              <Card  className="card" style={{ color : this.state.cardsColor[ele.index], minWidth: this.state.minWidth }} id={ele.index} >
                <div id="case"><Chips title={ele.keyWord} /><Switches id={ele.index} OnPassChecked={this.handleToggle}  /></div>
                <div >
                  <b>{ele.cardType}:</b>
                </div>
                <div >
                  <b>{ele.cardValue}</b>
                </div>
               </Card>
            ))}
          </div>
           );
     }
    }

    export default Demo;