import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Switches from '../switches.js'
import Chips from '../chips.js'


function createData(listData, index) {
  var type = listData.type
  var name = listData.name
  var url = listData.url
  return { index, type,name, url } ;
  }

var cardsData = [
  {
    "type" : "judge",
    "name" : "mahajan",
    "url"  : "#"
  }
,
{
  "type" : "judge",
  "name" : "mahajan",
  "url"  : "#"
}].map((ele, ind) => createData(ele, ind) );  

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
this.printActiveCardsInfo = this.printActiveCardsInfo.bind(this)
}

printActiveCardsInfo(){
  for(var i =0;i<cardsData.length;i++ ){
    if(this.state.cardsColor[i]=='')
     console.log(cardsData[i])
    else
     continue;
  }
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
  this.printActiveCardsInfo();
}
 
render() {
     return (
          <div id="content" className="flex-container">
            {cardsData.map( ele   => (
              <Card  className="card" style={{ color : this.state.cardsColor[ele.index], minWidth: this.state.minWidth }} id={ele.index} >
                <div id="case"><Chips title={ele.type} /><Switches id={ele.index} OnPassChecked={this.handleToggle}  /></div>
                <div >
                  <b>{ele.name}</b>
                </div>
              </Card>
            ))}
          </div>
           );
     }
    }

    export default Demo;