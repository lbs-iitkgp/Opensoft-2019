import React,{Component} from 'react';
import Card from './card.js';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js'

class Output extends Component {
    render(){
        return(
            <div>
                <Navbar />
                <Card />
                <br /><br />
                <AdvFilter />
            </div>
        );
    }
}

export default Output;