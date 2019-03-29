import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";


function createData(list, index) {
   var Judgement = list.Judgement;
   var Judge = list.Judge;
   var Date = list.Date;
   var url = list.url;
    return { index, Judgement,Judge, Date,url } ;
  }

var cardsData = [
  {
    "Judgement" : "appeal",
    "Judge"     : "mahajan",
    "Date"      : "12-12-12",
    "url"       : "#"
  }
       
].map((ele, ind) => createData(ele, ind) );  

class ResultCard extends Component{
  constructor(...props){
    super(...props);
  this.state = {
    minWidth  : 400,
    color : '',
    fontSize: 14,
    marginBottom: 12,
    padding : 10,
    margin :10,
    }
}

render() {
     return (
          <div id="cards2" >
            {cardsData.map( ele => (
              <Card  className="card" style={{ color : this.state.color }}  >
                <div id="judgement">
                  <b>Judgement:</b> {this.props.judgement}
                </div>
                <div id="judge">
                 <b>Judge:</b> <a href={ele.url}>{this.props.judge}</a> 
                </div>
                <div id="date">
                  <b>Date :</b> {this.props.date}
                </div>
                <br /><br />
              </Card>
            ))}
          </div>
           );
     }
     

    }

    export default ResultCard;