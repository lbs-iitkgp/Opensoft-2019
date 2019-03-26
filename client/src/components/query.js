import React, { Component } from 'react';
import TextField from '@material-ui/core/TextField';
import Navbar from '../navbar.js'
  


class SearchBar extends Component{
    constructor(props){
      super(props);
     
      this.passQuery = this.passQuery.bind(this)
    }
  
    passQuery(event){
      var searchedQuery = event.target.value;
      this.props.OnQueryPass(searchedQuery);
      console.log('passQueryfunc in query.js' + searchedQuery)

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
      <div>
        <TextField
        fullWidth={true}
        id="outlined-name"
        label="Query"
        //className={classes.textField}
         defaultValue={this.props.defaultSearch}
        onChange={this.passQuery}
        placeholder="Search here..."
        margin="normal"
        variant="outlined"
        multiline={false}
      />
     </div>  
      );
    }
  }
   
export default SearchBar;