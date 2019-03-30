import React,{Component} from 'react'
import AdvTable from '../caseindiv/advtable.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'
import PieGraph from './pie.js'
import '../App.css'
import { components } from 'react-select/lib/components';
import axios from 'axios'
import { Textsms } from 'material-ui-icons';

// function createData(list, index) {
//   var Name = list[0];
//   var NumOfCases = list[1];
//   var Percentile = list[2];
//    return { index, Name,NumOfCases, Percentile  } ;
//  }

// var cardsData={
//   'name' : '1999',
//   'number_of_cases' : '1500',
//   'percentile' : '99'
//}

var dummy = {
  "name" : '',
  "no of cases" : '',
  "percentile" : '',
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
   json_data : dummy
   }

}

  componentWillMount(){
    var id = this.props.match.params.id
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/year/${id}`)
    .then( (response) => {
      console.log(response,"resp");
      this.setState({
        json_data : response.data
      })
            
    })
    .catch(function (error) {
      console.log(error);
   });
  }  

  render() {
    var pieurl = `year/${this.props.match.params.id}/piechart`
    var tableurl = `year/${this.props.match.params.id}/cases`
    var per = this.state.json_data["percentile"]
   // var per1 = per.toString()
    //console.log(typeof per1)
      //per1 = per1.slice(0,4)
      var per1 = per.toPrecision(4)
    console.log(per)
return(
       <div>
         <Navbar />
         <div id='judgeIndivRes'> 
          <div id="judgeLeftCol" >
           <Card  className="cardInJudge" style={{ color : this.state.color }}  >
               <div id="judgement">
                 <b>Years:</b> {this.state.json_data["name"]}
               </div>
               <div id="judge">
                 <b>Number of Cases:</b> {this.state.json_data["no of cases"]}
               </div>
               <div id="date">
                  <b>Percentile :</b> {per1}
               </div>
               
               <br /><br />
             </Card>
             <div id='piegraph'><PieGraph  /></div>
          </div>
          <AdvTable myurl={tableurl} />
         </div>
       </div>
          );
    }
    

   }

   export default YeardsIndiv;