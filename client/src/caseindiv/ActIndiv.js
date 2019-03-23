import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import AdvFilter from './advtable.js'
const styles = theme => ({
    root: {
      width: '100%',
    },
    heading: {
      fontSize: theme.typography.pxToRem(15),
      fontWeight: theme.typography.fontWeightRegular,
    },
  });

  function createSections(section,index){
    var secTitle = section[0];
    var secDes = section[1]
    return{index,secTitle,secDes}
  }

  var sectionsData =[
    ['section-1','this is description of sec-1'],
    ['section-2','this is description of sec-2'],
    ['section-3','this is description of sec-13']
  ].map((ele,ind)=>createSections(ele,ind));
  

  function ActIndiv(props) {
    const { classes } = props;

      return(
          <div className={classes.root}>
          {sectionsData.map(ele => (
            <ExpansionPanel>
              <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
                <Typography className={classes.heading}>
                 <h3>{ele.secTitle}</h3>
                </Typography>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
                <Typography>
                  {ele.secDes}   
                 </Typography>
              </ExpansionPanelDetails>
            </ExpansionPanel>

          ))}
            <AdvFilter />
          </div>
      );
    // return (
    //   <div className={classes.root}>
    //     <ExpansionPanel>
    //       <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
    //         <Typography className={classes.heading}><h3>sectionx-1</h3></Typography>
    //       </ExpansionPanelSummary>
    //       <ExpansionPanelDetails>
    //         <Typography>
    //           Act one descriotion   
    //         </Typography>
    //       </ExpansionPanelDetails>
    //     </ExpansionPanel>
    //     <ExpansionPanel>
    //       <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
    //         <Typography className={classes.heading}><h3>sectionx-2</h3></Typography>
    //       </ExpansionPanelSummary>
    //       <ExpansionPanelDetails>
    //         <Typography>
    //         Acts two decripton
    //         </Typography>
    //       </ExpansionPanelDetails>
    //     </ExpansionPanel>
    //     <ExpansionPanel>
    //       <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
    //         <Typography className={classes.heading}><h3>sectionx-3</h3></Typography>
    //       </ExpansionPanelSummary>
    //       <ExpansionPanelDetails>
    //         <Typography>
    //           Act one descriotion   
    //         </Typography>
    //       </ExpansionPanelDetails>
    //     </ExpansionPanel>
    //     <AdvFilter />
    //    </div>
    // );
  }
  
  
  export default withStyles(styles)(ActIndiv);
  
