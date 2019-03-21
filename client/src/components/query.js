import React, { Component } from 'react';
//import '/src/App.css';
// import PropTypes from 'prop-types';
// import deburr from 'lodash/deburr';
// import Downshift from 'downshift';
// import { makeStyles } from '@material-ui/styles';
import TextField from '@material-ui/core/TextField';
// import Popper from '@material-ui/core/Popper';
// import Paper from '@material-ui/core/Paper';
// import MenuItem from '@material-ui/core/MenuItem';
// import Chip from '@material-ui/core/Chip';

  class SearchBar extends Component{
    constructor(props){
      super(props);
      this.passQuery = this.passQuery.bind(this)
    }
  
    passQuery(event){
      var searchedQuery = event.target.value;
      this.props.OnQueryPass(searchedQuery);
  
    }
      
    render(){
        const styles = theme => ({
            container: {
              display: "flex",
              flexWrap: "wrap"
            },
            textField: {
              marginLeft: theme.spacing.unit,
              marginRight: theme.spacing.unit
            },
            dense: {
              marginTop: 16
            },
            menu: {
              width: 200
            }
          });
        
        
      return (
        <TextField
        fullWidth="true"
        id="outlined-name"
        label="Query"
        //className={classes.textField}
        defaultValue=""
        onChange={this.passQuery}
        placeholder="Search here..."
        margin="normal"
        variant="outlined"
        multiline="true"
      />
  
      );
    }
  }
   
export default SearchBar;