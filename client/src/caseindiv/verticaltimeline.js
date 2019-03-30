import { VerticalTimeline, VerticalTimelineElement }  from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import React, { Component } from 'react';
import '../App.css';
import ReadMoreAndLess from 'react-read-more-less';
import axios from 'axios'

// function createTimelineElement(TimelineELe,index){
//   var date = TimelineELe[0];
//   var description = TimelineELe[1];
//   return{index,date,description} 
// }

var dummy =[
  ['','']
 ]
class VerticalTimeline2 extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      data : dummy
    }
  }

  componentWillMount(){
    var self = this;
    // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}${self.props.myurl}`)
      .then(function (response) {
        self.setState({ data: response.data })
      })
      .catch(function (error) {
        // handle error
        console.log('error is ' + error);
      })
      .then(function () {
        // always executed
      });
  }

 render(){
   return(
   <div className='timeline'>
    <VerticalTimeline layout='1-column' >
    {Object.keys(this.state.data).map(ele => (
      <VerticalTimelineElement
      className="vertical-timeline-element--work"
      iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
    >
    <h3 className="vertical-timeline-element-title">{this.state.data[0][0]}</h3>
    <p> 
      <ReadMoreAndLess
          ref={this.ReadMore}
          className="read-more-content"
          charLimit={250}
          readMoreText="Read more"
          readLessText="Read less"
          >
            {this.state.data[0][1]}
      </ReadMoreAndLess>
     </p>
    </VerticalTimelineElement>
    ))}
    </VerticalTimeline>
   </div>
   );
 }

  
}

export default VerticalTimeline2;