import React,{Component} from 'react';
import Card from './card.js';
import AdvFilter from './advtable.js'

class Output extends Component {
    render(){
        return(
            <div>
                <Card />
                <br /><br />
                <AdvFilter />
            </div>
        );
    }
}

export default Output;