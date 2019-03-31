import React,{Component} from 'react';
import AdvFilter from './advtable.js';
import Navbar from '../navbar.js';
import BasicCards from './basicCards.js'
import '../App.css'
import SearchBar from '../components/query.js'
import Button from '@material-ui/core/Button';
import ReactDOM from 'react-dom';
import axios from 'axios';

class Output extends Component {
    
    constructor(props){
        super(props)
        this.state = {
            updatedQuery : '',
            defaultSearch: '',
            data: [],
            loaded : false
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
        // Axios.post(`${process.env.REACT_APP_BACKEND_ORIGIN}basic/output/${this.state.updatedQuery}`,{
        //     updatedQuery : this.state.updatedQuery
        // }) .then(function (response) {
        //     console.log(response);
        //   })
        //   .catch(function (error) {
        //     console.log(error);
        //   });
        console.log('func caled')
        this.props.history.push({
            pathname  : `${this.state.updatedQuery}`,
            state :{
                defaultSearch : this.state.updatedQuery
            }
        })
        this.callAxios(this.state.updatedQuery);   
    }
    
    callAxios(data){
        axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/search/basic/stage_1?query=${data}`).then((response) => {
            // console.log("cass",response);
            return response.data.map(ele => {
                return Object.entries(ele).map((ind) => ind[1])
            })
          })
          .then((sanit_pre) => {
            // console.log(sanit_pre, "per")
            let topass = [1,0,1,1,1,0,0,1];
            return sanit_pre.map( (case_e,id) => case_e.filter((ele, index) => topass[index]))
            // return sanit_pre
          })
          .then(sanit => {
            //   console.log(sanit, "dsdgh")
              this.setState({
                  data: sanit,
                  loaded : true
              })
          })
          .catch(function (error) {
            console.log(error);
          });
    }

    componentWillMount(){
        // var x = () => {};
        if(this.props.location.state === undefined){
            this.setState({
                defaultSearch : this.props.match.params.id,  
            })
            this.callAxios(this.props.match.params.id);
            
        } else {
            this.setState({
                defaultSearch : this.props.location.state.defaultSearch,  
            })
            this.callAxios(this.props.location.state.defaultSearch);
        }
        ReactDOM.unmountComponentAtNode(document.getElementById('root'));
         //axios part
         
  
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
                <BasicCards parState={this.state.defaultSearch}/>
                 <br /><br />
                { this.state.loaded ? <AdvFilter data={this.state.data}  /> : " " }
            </div> 

            );
    }
}

export default Output;