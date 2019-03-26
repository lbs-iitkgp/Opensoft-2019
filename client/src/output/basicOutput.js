import React,{Component} from 'react';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import BasicCards from './basicCards.js'
import '../App.css'
import SearchBar from '../components/query.js'
import Button from '@material-ui/core/Button';

class Output extends Component {
    
    constructor(props){
        super(props)
        this.state = {
            updatedQuery : ''
        }
        this.getUpdatedResults = this.getUpdatedResults.bind(this)
        this.PassUpdatedQuery = this.PassUpdatedQuery.bind(this)
    }
    
   
    PassUpdatedQuery(NewQuery){
        console.log(NewQuery);
        this.setState({
            updatedQuery : NewQuery
        })

    }

    getUpdatedResults(){
        console.log(this.state.updatedQuery)
    }

    render(){
        return(
            <div>
                <Navbar />
                <div id='updatedSearchPart'>
                    <SearchBar OnQueryPass={this.PassUpdatedQuery} defaultSearch = {this.props.location.state.defaultSearch}  />
                      <div id='updateButton'>
                        <Button variant="contained" color="primary" onClick={this.getUpdatedResults}  style={{width:'130px',height:'50px'}}>
                         Update
                        </Button  >
                      </div>
                </div>    
                <BasicCards />
                 <br /><br />
                <AdvFilter />
            </div> 

            );
    }
}

export default Output;