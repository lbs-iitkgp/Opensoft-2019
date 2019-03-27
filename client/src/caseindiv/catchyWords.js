import React,{Component} from 'react'
import AdvTable from '../caseindiv/advtable.js'
import Graph from './plot.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'



var cardsData=  {
  'name' : 'criminal',
  'number_of_cases' : '1500',
  'percentile' : '99'
}

class CatchyWords extends Component{
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
       <div>
         <Navbar />
         <div id='keyWordsResult'> 
          <div id="keyWordLeft" >
            <Card  className="cardInKeyWords" style={{ color : this.state.color }}  >
               <div id="judgement">
                 <b>Name:</b> {cardsData.name}
               </div>
               <div id="judge">
                 <b>Number of Cases:</b> {cardsData.number_of_cases}
               </div>
               <div id="date">
                  <b>Percentile :</b> {cardsData.percentile}
               </div>
               <br /><br />
             </Card>
             <Graph />
          </div>
            <AdvTable />
         </div>
       </div>
          );
    }
    

   }

   export default CatchyWords;