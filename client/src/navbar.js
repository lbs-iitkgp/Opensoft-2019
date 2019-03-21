import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import './App.css'
import { NavLink } from 'react-router-dom'

const styles = {
  root: {
    flexGrow: 1,
    
  },
  grow: {
    flexGrow: 1,
  },
  
};

function Navbar(props) {
  const { classes } = props;
  return (
    <div className={classes.root}>
      <AppBar  >
          <div id='searchTypes'>
          <NavLink to='/basic'><Button color="inherit" id='basic'>Basic Search</Button></NavLink> 
          <NavLink to='/'><Button color="inherit" id='adv'>Advanced Search</Button></NavLink>   
         </div>   
      </AppBar>
    </div>
  );
}


export default withStyles(styles)(Navbar);
