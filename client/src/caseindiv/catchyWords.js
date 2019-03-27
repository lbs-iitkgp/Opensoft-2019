import React,{Component} from 'react'
import AdvTable from '../caseindiv/advtable.js'
import Graph from './plot.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'
import axios from 'axios'


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
   data_json : {}
   }
}

componentWillMount() {
  var id = this.props.match.params.id;
  var self = this;
  axios.get(`http://localhost:5000/catchword/${id}`)
    .then(function (response) {
      // handle success
      self.setState({
        data_json : response.data
      })
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
    .then(function () {
      // always executed
    });

}

render() {
    return (
       <div>
         <Navbar />
         <div id='keyWordsResult'> 
          <div id="keyWordLeft" >
            <Card  className="cardInKeyWords" style={{ color : this.state.color }}  >
               <div id="judgement">
                 <b>Name:</b> {this.state.data_json.name}
               </div>
               <div id="judge">
                 <b>Number of Cases:</b> {this.state.data_json.number_of_cases}
               </div>
               <div id="date">
                  <b>Percentile :</b> {this.state.data_json.percentile}
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