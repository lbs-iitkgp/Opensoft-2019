import React, { Component } from 'react';
import Navbar from '../navbar.js'
import SearchBar from './query.js'
import Container from 'react-bootstrap/Container';
import Button from '@material-ui/core/Button';

var basicSearched;
      
class BasicSearch extends Component{
    constructor(props){
      super(props);
      
      this.state={
         basicSearched : '' 
      }
      
      this.PassQuery = this.PassQuery.bind(this)
      this.getBasicResult = this.getBasicResult.bind(this)
      
    }
  
    PassQuery(queryRes){
      this.setState({
        basicSearched : queryRes
      })
      console.log('in PassQuery in basicSearch.js' + this.state.basicSearched) 
  }

    getBasicResult(){
     
      console.log('came in getBasicREsult'+ this.state.basicSearched)
     
        this.props.history.push({
        pathname : '/basic/output',
        state : {
          defaultSearch : this.state.basicSearched,
        }
      });
      
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
        <SearchBar OnQueryPass={this.PassQuery} defaultSearch={this.props.searchedQuery}  />
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