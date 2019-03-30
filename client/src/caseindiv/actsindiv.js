import React,{Component} from 'react'
import Graph from './plot.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'
import Tabs from './tabs.js'
import Grid from '@material-ui/core/Grid';
import axios from 'axios'

var cardsData = {
    'name' : '',
    'year' : '',
    'type' : '',
    "recent_version": {
            "id": '',
            "name": ''
         },
         "abbreviation": ''

} 
     
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
   data_json : cardsData
   }
}

    componentWillMount() {
        var id = this.props.match.params.id;
        var self = this;
        // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
        axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/act/${id}`)
            .then(function (response) {
                self.setState({ data_json: response.data })
                
            })
            .catch(function (error) {
                // handle error
                console.log('error is ' + error);
            })
            .then(function () {
                // always executed
            });
            
    }

render() {
    var urlTable = `/act/${this.props.match.params.id}/cases`
    var urlPlot = `/act/${this.props.match.params.id}/plot_line`
    var recenturl = `/act/${this.props.match.params.id}`
    var yearurl   = `/year/${this.props.match.params.id}`  
    
    return (
       <div>
        <Navbar />
        <div id='actindiv'>
            <div id='actleft'>
            <Card  className="cardInActs" style={{ color : this.state.color }}  >
                <div id="ActName">
                 <b>Act Name :</b> {this.state.data_json.name}
                    </div>
                    <div id="Year">
                            <b>Year:</b> <a href={yearurl}>{this.state.data_json.year}</a>
                    </div>
                    <div id="Type">
                            <b>Type :</b> {this.state.data_json.type}
                    </div>
                    <div id="RecentVersion">
                            <b>Recent Version :</b> <a href={recenturl}>{this.state.data_json.recent_version.name}</a>
                    </div>
                    <div id="abbr">
                            <b>Abbreviation :</b> {this.state.data_json.abbreviation}
                    </div>
                   
                    <br /><br />
                    </Card>
                    <Graph myurl={urlPlot}/>
                    </div>
                    <div id='tabsInActs'><Tabs /></div>
                 </div>                 
       </div>
          );
    }
    

   }

   export default ResultCard;