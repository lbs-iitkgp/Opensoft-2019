import Tabs from 'react-bootstrap/Tabs'
import React,{Component} from 'react'
import Tab from 'react-bootstrap/Tab'

function createData(data, index) {
    return { index, data }
  }
  

var citedIn = [
    'case-1',
    'case-2',
    'case-1',
    'case-2',
    'case-1',
    'case-2',
  ].map((ele, ind) => createData(ele, ind));
  
  var citedOut = [
    'case-1',
    'case-2',
    'case-1',
    'ca-2',
    'case-1',
    'case-2',
  ].map((ele, ind) => createData(ele, ind));
  
  var Acts = [
    'case-1',
    'case-2',
    'cas1',
    'case-2',
    'case-1',
    'case-2',
  ].map((ele, ind) => createData(ele, ind));
  
  
class ControlledTabs extends React.Component {
    constructor(props, context) {
      super(props, context);
      this.state = {
        key: 'home',
      };
    }
  
    render() {
      return (
        <Tabs
          id="controlled-tab-example"
          activeKey={this.state.key}
          onSelect={key => this.setState({ key })}
        >
          <Tab eventKey="home" title="CASES CITED IN">
            <ul>
                {citedIn.map(ele => (<a href="#"><li>{ele.data}</li></a>))}
            </ul>
          </Tab>
          <Tab eventKey="profile" title="CASES CITED BY">
            <ul>
                {citedOut.map(ele => (<a href="#"><li>{ele.data}</li></a>))}
            </ul>
          </Tab>
          <Tab eventKey="contact" title="ACTS" >
            <ul>
                {Acts.map(ele => (<a href="#"><li>{ele.data}</li></a>))}
            </ul>
          </Tab>
        </Tabs>
      );
    }
  }
  
  export default ControlledTabs;