import React, { Component } from 'react';
import { MDBCol, MDBFormInline, MDBBtn } from "mdbreact";

class Judges extends Component{
    constructor(props){
      super(props);
      this.passDataJudges = this.passDataJudges.bind(this);
    }
  
    passDataJudges(event){
      var searchedJudge = event.target.value;
      this.props.OnJudgeNamePass(searchedJudge);
    }
    
    render(){
      const wrapperStyle = {  margin: 20 };
  
      return (
        <MDBCol md="12" style={wrapperStyle}>
          <h3> Judges </h3>
  
          <MDBFormInline className="md-form mr-auto mb-4">
            <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" id="judge"  onChange={this.passDataJudges} defaultValue = '' />
          </MDBFormInline>
        </MDBCol>
      );
    }
  }

  export default Judges;