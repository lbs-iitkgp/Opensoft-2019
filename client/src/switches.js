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
          onChange={this.handleChange}
          color="primary"
        />
      </div>
    );
  }
}

export default Switches;
