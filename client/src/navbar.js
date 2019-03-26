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
          <NavLink to='/basic' style={{ textDecoration: 'none' }} ><Button  id='basic'>Basic Search</Button></NavLink> 
          <div id='line'></div>
          <NavLink to='/' style={{ textDecoration: 'none' }} ><Button  id='adv'>Advanced Search</Button></NavLink>   
         </div>   
      </AppBar>
    </div>
  );
}


export default withStyles(styles)(Navbar);
