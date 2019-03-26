import React,{Component} from 'react';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import BasicCards from './basicCards.js'
import '../App.css'

class Output extends Component {
    render(){
        return(
            <div>
                <Navbar />
                <BasicCards />
                 <br /><br />
                <AdvFilter />
            </div> 

            );
    }
}

export default Output;