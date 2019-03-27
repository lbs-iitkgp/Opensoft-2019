import React,{Component} from 'react'
import AdvTable from '../caseindiv/advtable.js'
import Radar from './radar.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'


function createData(list, index) {
  var Name = list[0];
  var NumOfCases = list[1];
  var Percentile = list[2];
   return { index, Name,NumOfCases, Percentile  } ;
 }

var cardsData={
  'name' : '1999',
  'number_of_cases' : '1500',
  'percentile' : '99'
}

class YeardsIndiv extends Component{
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
         <div id='judgeIndivRes'> 
          <div id="judgeLeftCol" >
           
             <Card  className="cardInJudge" style={{ color : this.state.color }}  >
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
            <Radar />
          </div>
          <AdvTable />
         </div>
       </div>
          );
    }
    

   }

   export default YeardsIndiv;