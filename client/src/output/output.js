import React,{Component} from 'react';
import AdvCards from './advCards.js';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import Drawer from './drawer.js';
import '../App.css'
import ScrollUpButton from "react-scroll-up-button"; 


class Output extends Component {
    
    render(){
          
        return(
            <div id='output-advanced'>
                
                {/* <Navbar /> */}
                {/* <Drawer FromParent={this.props.location.state.defaultAdvSearch} /> */}
              <AdvCards />
                <br /><br />
              <div id='tableInOutput'><AdvFilter /></div>
              <ScrollUpButton />
            </div> 

            );
    }
}

export default Output;