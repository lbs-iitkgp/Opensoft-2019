import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Chips from '../chips.js'
import Switches from '../switches.js'


function createData(listData, index) {
  var Case = listData[0];
  var Judgement = listData[1];
  var Judge = listData[2];
  var Act = listData[3];
  var Category = listData[4];
  var Date = listData[5];
  return { index, Case, Judgement, Judge, Act, Category, Date  } ;
  }

var cardsData = [
    ["mycase",
    "appeal",
    "mahajan",
    "indian stamp act",
    "criminal",
    "12-12-12"]
  ,
  ["mycase",
    "appeal",
    "mahajan",
    "indian stamp act",
    "criminal",
    "12-12-12"
  ]
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
                <div id="case"><h2 href="#"> {ele.Case}</h2><Switches id={ele.index} OnPassChecked={this.handleToggle}  /></div>
                <div id="judgement">
                  <b>Judgement:</b> {ele.Judgement}
                </div>
                <div id="judge">
                  <b>Judge:</b> {ele.Judge}
                </div>
                <div id="act">
                  <b>Act cited:</b> {ele.Act}
                </div>
                <div id="category">
                  <b>Category : </b> {ele.Category}
                </div>
                <div id="date">
                  <b>Date :</b> {ele.Date}
                </div>
                <br /><br />
                <Chips />    
               </Card>
            ))}
          </div>
           );
     }
     

    }

    export default Demo;