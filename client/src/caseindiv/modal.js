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
import CitedCases from './citedCases.js'
import ScrollUpButton from "react-scroll-up-button"; 
import {Component} from 'react'
import axios from 'axios'


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
    json_data : {},
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
    var self = this;
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/modal/${id}`)
    .then(function (response) {
      self.setState({data_json : response.result})
    })
    .catch(function (error) {
      // handle error
      console.log('error is '+error);
    })
    .then(function () {
      // always executed
    }); 
    console.log(this.state.json_data)  
}

  
    

  render(){
    return(
     <div >
       <AppBar  id='fixedTitle'>
          <Toolbar>
            <Typography variant="h6" color="inherit" >
              {this.state.json_data.case_name}
            </Typography>
          </Toolbar>
         </AppBar>
          <div id='contain'>
            <div id='left-indiv'>
              <div id ='resCard'><ResultCard  judgement={this.state.json_data.case_judgement} judge={this.state.json_data.case_judge} date={this.state.json_data.case_date}/></div> 
              <div id='graph'>< Area /></div>
            </div>
            <div id='vtl'>
              <VerticalTimeline />
            </div>
            <div id='actchips'>
              <CitedCases />
            </div>
          </div>
        <ScrollUpButton />
     </div>
      );
  }


}


export default FullScreenDialog;


