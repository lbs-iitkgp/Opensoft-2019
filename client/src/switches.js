import React, { Component } from "react";
import Switch from "@material-ui/core/Switch";

class Switches extends Component {
  constructor(props) {
    super(props);
    this.state = {
      switchState: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
  //  if(!this.state.switchState) {
  //     this.setState({
  //       switchState : true
  //     })
  //  }
  //  else{
  //   this.setState({
  //     switchState : false
  //   })
  //  }
   this.setState({
     switchState : !this.state.switchState
   })
   this.props.OnPassChecked(this.state.switchState, this.props.id)
  }

  componentWillMount(){
    this.setState({
      switchState : true
    })
  }

  render() {
    return(
      <div>
        <Switch
         checked = {this.state.switchState}
         //checked = {{checked : true}}
          onChange={this.handleChange}
          color="primary"
        />
      </div>
    );
  }
}

export default Switches;
