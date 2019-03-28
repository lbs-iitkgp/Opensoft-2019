import React,{Component} from 'react'
import Graph from './plot.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'
import Tabs from './tabs.js'
import Grid from '@material-ui/core/Grid';
import axios from 'axios'

var cardsData = {
    'name' : 'Indian stamp Act',
    'year' : '2010',
    'type' : 'Central',
    "recent_version": {
            "id": '1',
            "name": 'indo act'
         },
         "abbreviation": 'irctc'

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
   cardsData : {}
   }
}

componentWillMount(){
    console.log("mount");
    var id = this.props.match.params.id;
    var self = this;
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/act/${id}`)
        .then(function (response) {
            self.setState({ cardsData : response.data });
            console.log("Aadi",response.data);
        })
        .catch(function (error) {
            // handle error
            console.log('error is ' + error);
        })
        .then(function () {
            // always executed
        });
    //console.log(this.state.json_data) 
}

render() {
    console.log("render",this.state.cardsData);
    return (
       <div>
        <Navbar />
        <div id='actindiv'>
            <div id='actleft'>
            <Card  className="cardInActs" style={{ color : this.state.color }}  >
                <div id="ActName">
                 <b>Act Name :</b> {cardsData.name}
                    </div>
                    <div id="Year">
                        <b>Year:</b> <a href="#">{this.state.cardsData.year}</a>
                    </div>
                    <div id="Type">
                            <b>Type :</b> {this.state.cardsData.type}
                    </div>
                    <div id="RecentVersion">
                            <b>Recent Version :</b> <a href="#">{this.state.cardsData.recent_version.name}</a>
                    </div>
                    <div id="abbr">
                            <b>Abbreviation :</b> {this.state.cardsData.abbreviation}
                    </div>
                   
                    <br /><br />
                    </Card>
                    <Graph />
                    </div>
                    <div id='tabsInActs'><Tabs /></div>
                 </div>                 
       </div>
          );
    }
    

   }

   export default ResultCard;