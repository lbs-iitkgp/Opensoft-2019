import { VerticalTimeline, VerticalTimelineElement }  from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import React, { Component } from 'react';
import '../App.css';

function createTimelineElement(TimelineELe,index){
  var date = TimelineELe[0];
  var description = TimelineELe[1];
  return{index,date,description} 
}

var timelineData = [
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
  ['12-12-12',' Creative Direction, User Experience, Visual Design, Project Management, Team Leading'],
].map((ele,ind) => createTimelineElement(ele,ind));

class VerticalTimeline2 extends React.Component{
 render(){
   return(
   <div className='timeline'>
    <VerticalTimeline layout='1-column' >
    {timelineData.map(ele => (
      <VerticalTimelineElement
      className="vertical-timeline-element--work"
      iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
    >
    <h3 className="vertical-timeline-element-title">{ele.date}</h3>
    <p>{ele.description}</p>
    </VerticalTimelineElement>
    ))}
    </VerticalTimeline>
   </div>
   );
 }

  // render(){
//     return(
//    <div className='timeline'>
//  <VerticalTimeline layout='1-column' >
//   <VerticalTimelineElement
//     className="vertical-timeline-element--work"
//     iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
//   >
//      <h3 className="vertical-timeline-element-title">Date : 12-12-12</h3>
//     <p> 
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading

//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     className="vertical-timeline-element--work"
//    iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
    
//   >
//      <h3 className="vertical-timeline-element-title">Date : 12-12-12</h3>
//     <p> 
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading
//       Creative Direction, User Experience, Visual Design, Project Management, Team Leading

//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     className="vertical-timeline-element--work"
//     date="2008 - 2010"
//     iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
   
//   >
//     <h3 className="vertical-timeline-element-title">Web Designer</h3>
//     <h4 className="vertical-timeline-element-subtitle">Los Angeles, CA</h4>
//     <p>
//       User Experience, Visual Design
//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     className="vertical-timeline-element--work"
//     date="2006 - 2008"
//    >
//     <h3 className="vertical-timeline-element-title">Web Designer</h3>
//     <h4 className="vertical-timeline-element-subtitle">San Francisco, CA</h4>
//     <p>
//       User Experience, Visual Design
//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     className="vertical-timeline-element--education"
//     date="April 2013"
//     >
//     <h3 className="vertical-timeline-element-title">Content Marketing for Web, Mobile and Social Media</h3>
//     <h4 className="vertical-timeline-element-subtitle">Online Course</h4>
//     <p>
//       Strategy, Social Media
//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     className="vertical-timeline-element--education"
//     date="November 2012"
//     >
//     <h3 className="vertical-timeline-element-title">Agile Development Scrum Master</h3>
//     <h4 className="vertical-timeline-element-subtitle">Certification</h4>
//     <p>
//       Creative Direction, User Experience, Visual Design
//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     className="vertical-timeline-element--education"
//     date="2002 - 2006"
//     >
//     <h3 className="vertical-timeline-element-title">Bachelor of Science in Interactive Digital Media Visual Imaging</h3>
//     <h4 className="vertical-timeline-element-subtitle">Bachelor Degree</h4>
//     <p>
//       Creative Direction, Visual Design
//     </p>
//   </VerticalTimelineElement>
//   <VerticalTimelineElement
//     />
// </VerticalTimeline>
// </div>
// );
//     }
}

export default VerticalTimeline2;