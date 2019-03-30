import Tabs from 'react-bootstrap/Tabs'
import React, { Component } from 'react'
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
      citedin : citedIn,
      citedout : citedOut,
      acts : Acts
    };
  }

  componentWillMount(){
    var self = this;
    // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}${self.props.myurl}`)
      .then(function (response) {
        self.setState({ 
          acts : response.data.cited_acts,
          citedin : response.data.cited_by_cases,
          citedout: response.data.cited_cases
        })
      })
      .catch(function (error) {
        // handle error
        console.log('error is ' + error);
      })
      .then(function () {
        // always executed
      });
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
            {Object.keys(this.state.citedin).map(ele => (<a href="#"><li>{this.state.citedin[ele]}</li></a>))}
          </ul>
        </Tab>
        <Tab eventKey="profile" title="CASES CITED BY">
          <ul>
            {Object.keys(this.state.citedout).map(ele => (<a href="#"><li>{this.state.citedout[ele]}</li></a>))}
          </ul>
        </Tab>
        <Tab eventKey="contact" title="ACTS" >
          <ul>
            {Object.keys(this.state.acts).map(ele => (<a href="#"><li>{this.state.acts[ele]}</li></a>))}
          </ul>
        </Tab>
      </Tabs>
    );
}

export default ControlledTabs;