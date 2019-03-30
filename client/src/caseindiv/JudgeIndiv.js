import React,{Component} from 'react'
import AdvTable from '../caseindiv/advtable.js'
import Graph from './plot.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'
import axios from 'axios'

var dummy = { "name": "", "number_of_cases": "","percentile":""};

class ResultCard extends Component{
 constructor(...props){
   super(...props);
   this.state = {
   minWidth  : 400,
   minHeight : 80,
   color : '',
   fontSize: 30,
   //marginBottom: 12,
   //padding : 10,
   margin :10,
   data_json : dummy
   }
}



componentWillMount(){
   var id = this.props.match.params.id;
    var self = this;
    // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
    .then(function (response) {
      self.setState({data_json : response.data})
    })
    .catch(function (error) {
      // handle error
      console.log('error is '+error);
    })
    .then(function () {
      // always executed
    });   
}

render() {
    var urlTable = `judge/${this.props.match.params.id}/cases`
    var urlPlot = `/judge/${this.props.match.params.id}/plot_line`
    //alert(url);
    return (
       <div>
         <Navbar />
         <div id='judgeIndivRes'> 
          <div id="judgeLeftCol" >
           
             <Card  className="cardInJudge" style={this.state}  >
               <div id="judgement">
                 <b>Name:</b> {this.state.data_json.name}
               </div>
               <div id="judge">
                 <b>Number of Cases:</b> {this.state.data_json["no of cases"]}
               </div>
               <div id="date">
                  <b>Percentile :</b> {this.state.data_json.percentile}
               </div>
               <br /><br />
             </Card>
          
          <Graph myurl={urlPlot}/>
          </div>
          <AdvTable myurl={urlTable} />
         </div>
       </div>
          );
    }
    

   }

   export default ResultCard;