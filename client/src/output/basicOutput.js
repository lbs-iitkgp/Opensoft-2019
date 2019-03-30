import React,{Component} from 'react';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import BasicCards from './basicCards.js'
import '../App.css'
import SearchBar from '../components/query.js'
import Button from '@material-ui/core/Button';
import ReactDOM from 'react-dom';
import Axios from 'axios';

class Output extends Component {
    
    constructor(props){
        super(props)
        this.state = {
            updatedQuery : '',
            defaultSearch: ''
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
        //console.log(this.state.updatedQuery)
        Axios.post(`${process.env.REACT_APP_BACKEND_ORIGIN}basic/output/${this.state.updatedQuery}`,{
            updatedQuery : this.state.updatedQuery
        }) .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
        
        this.props.history.push({
            pathname  : `/basic/output/${this.state.updatedQuery}`,
            state :{
                defaultSearch : this.state.updatedQuery
            }
        })

        
    }

    componentWillMount(){
        // var x = () => {};
        if(this.props.location.state === undefined){
            this.setState({
                defaultSearch : this.props.match.params.id,  
            })
        } else {
            this.setState({
                defaultSearch : this.props.location.state.defaultSearch,  
            })
        }
        ReactDOM.unmountComponentAtNode(document.getElementById('root'));
    }

    

            

    render(){
        return(
            <div>
                <Navbar />
                <div id='updatedSearchPart'>
                    <SearchBar OnQueryPass={this.PassUpdatedQuery} defaultSearch={this.state.defaultSearch} />
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