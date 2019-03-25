import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";


function createData(list, index) {
   var Judgement = list[0];
   var Judge = list[1];
   var Date = list[2];
    return { index, Judgement,Judge, Date  } ;
  }

var cardsData = [
    ['appeal','mahajan','12-12-12'],
   
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
                  <b>Judgement:</b> {ele.Judgement}
                </div>
                <div id="judge">
                  <b>Judge:</b> {ele.Judge}
                </div>
                <div id="date">
                  <b>Date :</b> {ele.Date}
                </div>
                <br /><br />
              </Card>
            ))}
          </div>
           );
     }
     

    }

    export default ResultCard;