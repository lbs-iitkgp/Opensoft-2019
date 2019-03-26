import React,{Component} from 'react';
import AdvCards from './advCards.js';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import Drawer from './drawer.js';
import '../App.css'

class Output extends Component {
    render(){
        return(
            <div>
                <Navbar />
                <Drawer FromParent={this.props.location.state.defaultAdvSearch} />
                <AdvCards />
                <br /><br />
                <div id='tableInOutput'><AdvFilter /></div>
            </div> 

            );
    }
}

export default Output;