import React from 'react';
import { makeStyles } from '@material-ui/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import CloseIcon from '@material-ui/icons/Close';
import Slide from '@material-ui/core/Slide';
import ResultCard from './jjd.js'
import '../App.css'
import VerticalTimeline from './verticaltimeline.js'
import Area from './plot.js'
import CitedCases from './cited_Case_Cpoy.js'
import ScrollUpButton from "react-scroll-up-button"; 
import {Component} from 'react'
import axios from 'axios'
import Navbar from '../navbar.js'

var JudgeName=''
,Judgement='',
CaseDate='',CaseName='';


function Transition(props) {
  return (<Slide direction="up" {...props} />)
}

const useStyles = makeStyles({
  appBar: {
    position: 'fixed',
  },
  flex: {
    flex: 1,
  },
});

  
class FullScreenDialog extends Component {
 
 constructor(props){
  super(props)
  this.state={
     Judge_Name : '',
     Judgement_1 : '',
     Case_Date :'',
     Case_Name : ''
   }
  // this.handleClickOpen = this.handleClickOpen.bind(this)
  // this.handleClose = this.handleClose.bind(this)
 }
 
  //const classes = useStyles();
  //const [open, setOpen] = React.useState(false);
  
  //  handleClickOpen() {
  //   setOpen(true);
  // }

  //  handleClose() {
  //   setOpen(false);
  // }

  componentWillMount(){
   var id = this.props.match.params.id;
    
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/case/${id}`)
    .then(response => {
      console.log(response.data)
      var judge_name = response.data.judges.map(a => a.name).join(',')
       
      JudgeName = judge_name
      Judgement = response.data.judgement
      CaseDate = response.data.date
      console.log(response.data.name,"respone.data.name")
      CaseName = response.data.name
      console.log(CaseName)
      this.setState({
        Judge_Name : JudgeName,
        Judgement_1 : Judgement,
        Case_Date : CaseDate,
        Case_Name : CaseName
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

  
    

  render(){
    //console.log("Aadi",this.state.json_data);
    var urlPlot = `/case/${this.props.match.params.id}/plot_line`
    var urlTimeline = `/case/${this.props.match.params.id}/timeline`
    var urlCase = `/case/${this.props.match.params.id}/citations`
    return(
     <div >
       <Navbar />
       <br />
       <div id='contain'>
            <div id='left-indiv'>
              <div id ='resCard'><ResultCard casename={this.state.Case_Name}  judgement={this.state.Judgement_1} judge={this.state.Judge_Name} date={this.state.Case_Date}/></div> 
              <div id='graph'>< Area myurl={urlPlot}/></div>
            </div>
            <div id='vtl'>
              <VerticalTimeline myurl={urlTimeline}/>
            </div>
            <div id='actchips'>
              <CitedCases myurl={urlCase}/>
            </div>
          </div>
        <ScrollUpButton />
     </div>
      );
  }


}


export default FullScreenDialog;


