import React, { Component } from 'react';
import TextField from '@material-ui/core/TextField';
import Navbar from '../navbar.js'
import SearchBar from './query.js'
import Container from 'react-bootstrap/Container';
import Button from '@material-ui/core/Button';

var basicSearched;
      
class BasicSearch extends Component{
    constructor(props){
      super(props);
      this.passQuery = this.passQuery.bind(this)
      this.getBasicResult = this.getBasicResult.bind(this)
    }
  
    passQuery(queryRes){
      basicSearched = queryRes;
  }

    getBasicResult(){
      console.log(basicSearched);
      this.props.history.push("/basic/output");
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
         <Navbar />
        <br /><br />
         <Container id='box_shadow'> 
        <h3>Search</h3>
        <SearchBar OnQueryPass={this.passQuery}   />
        <div className='searchButton'>
          <Button variant="contained" color="primary" onClick={this.getBasicResult}  style={{width:'130px',height:'50px'}}>
            Search
          </Button  >
        </div>      
        </Container>
       </div>
      );
    }
  }
   
export default BasicSearch;