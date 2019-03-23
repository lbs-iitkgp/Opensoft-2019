import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Chips from './chips.js'

function createActs(act,index){
  return {index,act}
}

var Acts = [
  'act no.1 section 1',
  'act no.21 section 2',
  'act no.13 section 31',
].map((ele,ind)=> createActs(ele,ind));

class ActChips extends Component{
  constructor(...props){
    super(...props);
  this.state = {
    minWidth  : 400, 
    minHeight : 200,
    color : '',
    fontSize: 14,
    marginBottom: 12,
    padding : 10,
    margin :10,
   }

}

render(){
  return(
        <div id="content" className='flex-container'>
          <Card className='card' style={{ color : this.state.color, minWidth : this.state.minWidth,minHeight:this.state.minHeight}} >
          {Acts.map(ele => (
            <Chips actName={ele.act} />
        ))}
          </Card> 
         </div>
  );
}

// render() {
//      return (
//           <div id="content" className="flex-container">
//             <Card  className="card" style={{ color : this.state.color, minWidth : this.state.minWidth,minHeight:this.state.minHeight}}      >
//                 <Chips actName='indian stamp act in the  year 2010202' />  
//                 <Chips actName='indian sta acts for he dndnienien' />
//                 <Chips actName='indian stp acts jnjrngrngirgiri' />  
//                 <Chips actName='indian stp acts jnjrngrngirgiri' />  
//             </Card>
//             </div>
//            );
//      }
     

    }

    export default ActChips;