import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Chips from '../chips.js'
import 'material-ui-icons'


function createData(listData, index) {
  
  var type = listData.type;
  var name = listData.name;
  var url = listData.url;
  return { index, type, name, url } ;
  }

var cardsData = [
  {
    "type" : 'judge',
    "name" : 'mahjan',
    "url" : '#',
    
  }
,
{
  "type" : 'judge',
  "name" : 'mahjan',
  "url" : '#',
  
}].map((ele, ind) => createData(ele, ind) );  


class Demo extends Component{
  constructor(...props){
    super(...props);
  this.state = {
    minWidth  : 300,
    color : '',
    fontSize: 14,
    marginBottom: 12,
    padding : 10,
    margin :10,
    cardsColor : ['','']
  }
this.handleToggle = this.handleToggle.bind(this);
this.removeCard = this.removeCard.bind(this);
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

removeCard(id){
    let removeC = () => {
        const localId = id;
        var content = document.getElementById(localId)
        content.remove()
     }
    return removeC;
}

render() {
     return (
          <div id="content" className="flex-container">
            {cardsData.map( ele => (
              <Card  className="card" style={{ color : this.state.cardsColor[ele.index],minWidth : this.state.minWidth }} id={ele.index} >
                <div id='chipCross'><Chips title={ele.type} /><i class="material-icons md-48" onClick={this.removeCard(ele.index)} >highlight_off</i></div>
                 <div id="cardType">
                  <a href={ele.url}><b><h3>{ele.name}:</h3></b></a> 
                </div>
              </Card>
            ))}
          </div>
           );
     }
     

    }

    export default Demo;