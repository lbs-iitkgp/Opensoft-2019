import React,{Component} from 'react';
import AdvCards from './advCards.js';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import Drawer from './drawer.js';
import '../App.css'
import ScrollUpButton from "react-scroll-up-button"; 
import ReactDOM from 'react-dom';
import axios from 'axios'


class Output extends Component {
    constructor(props){
      super(props);
        this.state = {
          data :[ ['Gabby George', 'Business Analyst', 'Minneapolis', 30, '$100,000'],
          ['Aiden Lloyd', 'Business Consultant', 'Dallas', 55, '$200,000'],
          ['Jaden Collins', 'Attorney', 'Santa Ana', 27, '$500,000'],
          ['Franky Rees', 'Business Analyst', 'St. Petersburg', 22, '$50,000'],
          ['Aaren Rose', 'Business Consultant', 'Toledo', 28, '$75,000'],
          ['Blake Duncan', 'Business Management Analyst', 'San Diego', 65, '$94,000'],
          ['Frankie Parry', 'Agency Legal Counsel', 'Jacksonville', 71, '$210,000'],
          ['Lane Wilson', 'Commercial Specialist', 'Omaha', 19, '$65,000'],
          ['Robin Duncan', 'Business Analyst', 'Los Angeles', 20, '$77,000'],
          ['Mel Brooks', 'Business Consultant', 'Oklahoma City', 37, '$135,000']
            ],
          columns : ['MyName', 'Title', 'Location', 'Age', 'Salary'],
        };
        this.getDataCards = this.getDataCards.bind(this);
      }
    
      // getDataCards(activeones){
      //   axios.post(`${process.env.REACT_APP_BACKEND_ORIGIN}/search/basic/stage_2`,activeones)
      //   .then((response)=>{
      //       this.setState({
      //         data : response.data,
      //         columns : Object.keys(response.data[0])
      //       })
      //     }).catch((error)=>{
      //       console.log(error);
      //     });
      // }

      componentWillMount(){
        // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/search/cards?query`)
        // .then((response)=>{
        //     this.setState({
        //       data : response.data,
        //       columns : Object.keys(response.data[0])
        //     })
        //   }).catch((error)=>{
        //     console.log(error);
        //   });
      }
    
     
    render(){
          
        return(
            <div id='output-advanced'>
                
                {/* <Navbar /> */}
                {/* <Drawer FromParent={this.props.location.state.defaultAdvSearch} /> */}
              <AdvCards cardQuery={this.props.cardQuery}  onAdvCardsPass={this.getDataCards}/>
                <br /><br />
              <div id='tableInOutput'><AdvFilter caseData={this.props.caseData} /></div>
              <ScrollUpButton />
            </div> 

            );
    }
}

export default Output;