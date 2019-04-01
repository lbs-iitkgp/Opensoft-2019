import React, { Component } from 'react';
import {useState} from 'react'
import { withStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import '../App.css'
import axios from 'axios'

var titles = new Array ();
var descris = new Array ();
       
const styles = theme => ({
    root: {
      width: '100%',
      minWidth: 400,
      fontSize: 30
    },
    heading: {
      fontSize: theme.typography.pxToRem(15),
      fontWeight: theme.typography.fontWeightRegular,
    },
  });

  function createSections(section,index){
    
    
    var a = window.location.href.length-1
      var id = window.location.href[a]
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/act/${id}/sections`)
    .then( (response) => {
      titles = response
      for(var i=0;i<titles.length;i++){
        axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/act/${id}/section/${i}`)
      .then((response) =>{
        descris.push(response.data.section_text)
           
      })
      .catch( (error) => {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });   
  }    
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
    .then(function () {
      // always executed
    });
    
    
   

}
   

  
  
  
   
 
  function ActsAccord(props,title,desc) {
    const { classes } = props;
     var nums = new Array ()
    for(var j=0;j<titles.length;j++){
    nums[j] = j;
    }

      return(
          <div className={classes.root}>
          {nums.map(ele => (
            <ExpansionPanel>
              <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
                <Typography className={ele}>
                 <h3>{ele}</h3>
                </Typography>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
                <Typography id='act_sec'>
                  {ele}
                 </Typography>
              </ExpansionPanelDetails>
            </ExpansionPanel>

          ))}
           </div>
      );
    
  }
  
  
  export default withStyles(styles)(ActsAccord);
  
