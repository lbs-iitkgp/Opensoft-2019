import React,{Component} from 'react';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import BasicCards from './basicCards.js'
import '../App.css'
import BasicSearch from '../components/basicSearch.js'
import SearchBar from '../components/query.js'
import Button from '@material-ui/core/Button';

class Output extends Component {
    
    constructor(props){
        super(props)
        this.state = {
            defaultSearched : ''
        }
        this.setDefault = this.setDefault.bind(this)
    }
    
    setDefault(searchedQuery){
         this.setState({
             defaultSearched : searchedQuery
         })
         console.log('enterred setDefault FUnc')
    }

    render(){
        return(
            <div>
                <Navbar />
                <BasicSearch searchedQuery={this.props.location.state.defaultSearch} />
                <BasicCards />
                 <br /><br />
                <AdvFilter />
            </div> 

            );
    }
}

export default Output;