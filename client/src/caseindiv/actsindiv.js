import React,{Component} from 'react'
import Radar from './radar.js'
import Graph from './plot.js'
import Card from "@material-ui/core/Card"
import '../App.css'
import Navbar from '../navbar.js'
import Tabs from './tabs.js'
import Grid from '@material-ui/core/Grid';

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
   }
}

render() {
    return (
       <div>
        <Navbar />
            <Grid container spacing={12}>
                <Grid item xs={3}>
                    <Card  className="cardInActs" style={{ color : this.state.color }}  >
                    <div id="ActName">
                        <b>Act Name :</b> {cardsData.name}
                    </div>
                    <div id="Year">
                        <b>Year:</b> {cardsData.year}
                    </div>
                    <div id="Type">
                        <b>Type :</b> {cardsData.type}
                    </div>
                    <div id="RecentVersion">
                        <b>Recent Version :</b> {cardsData.recent_version.name}
                    </div>
                    <div id="abbr">
                        <b>Abbreviation :</b> {cardsData.abbreviation}
                    </div>
                   
                    <br /><br />
                    </Card>
                    <Graph />
                    <Radar />
                 </Grid>
                 <Grid item xs={9}>
                    <div id='tabsInActs'><Tabs /></div>
                 </Grid>
            </Grid>
       </div>
          );
    }
    

   }

   export default ResultCard;