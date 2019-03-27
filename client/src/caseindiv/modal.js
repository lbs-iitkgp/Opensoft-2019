import React from 'react';
import { makeStyles } from '@material-ui/styles';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
  import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
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

const useStyles = makeStyles({
  appBar: {
    position: 'fixed',
  },
  flex: {
    flex: 1,
  },
});

function Transition(props) {
  return <Slide direction="up" {...props} />;
}

function FullScreenDialog() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  function handleClickOpen() {
    setOpen(true);
  }

  function handleClose() {
    setOpen(false);
  }

  return (
    <div >
      
        <AppBar className={classes.appBar} id='fixedTitle'>
          <Toolbar>
              <Typography variant="h6" color="inherit" className={classes.flex}>
              Title of the Case
              </Typography>
            <IconButton color="inherit" onClick={handleClose} aria-label="Close">
              <CloseIcon />
            </IconButton>
          </Toolbar>
        </AppBar>
         <div id='contain'>
         <div id='left-indiv'>
            <div id ='resCard'><ResultCard /></div> 
            <div id='graph'>< Area /></div>
         </div>
          <div id='vtl'>
            <VerticalTimeline />
          </div>
          <div id='actchips'>
             <CitedCases />
          </div>
        </div>
        </div>
  );
}

export default FullScreenDialog;


