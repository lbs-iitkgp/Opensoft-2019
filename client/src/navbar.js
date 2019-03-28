import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import './App.css'
import { NavLink } from 'react-router-dom'
import Typography from 'material-ui/Typography';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import SaveIcon from '@material-ui/icons/Save';
import EditIcon from '@material-ui/icons/Edit';

const styles = {
  root: {
    flexGrow: 1,
    
  },
  grow: {
    flexGrow: 1,
  },
  // This group of buttons will be aligned to the right
  rightToolbar: {
    marginLeft: 'auto',
    marginRight: -12,
  },
  menuButton: {
    marginRight: 16,
    marginLeft: -12,
  },
  
};

function Navbar(props) {
  const { classes } = props;
  return (
    <div className={classes.root} id="homepageNavbar">
   <AppBar position="static">
    <Toolbar>
      <Typography variant="title" color="inherit">Lawbrarian</Typography>

      <section className={classes.rightToolbar}>

        <NavLink to='/basic' style={{ textDecoration: 'none' }} ><a id='basic'>Basic Search</a></NavLink>
        <NavLink to='/' style={{ textDecoration: 'none' }} ><a id='adv'>Advanced Search</a></NavLink>

      </section>
    </Toolbar>
  </AppBar>
   </div>
  );
}

export default withStyles(styles)(Navbar);
