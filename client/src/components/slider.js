import React from 'react';
import 'antd/dist/antd.css';
import {Slider} from 'antd';

class YearsSlider extends React.Component {
  constructor(props){
    super(props);
    this.sliderChange = this.sliderChange.bind(this)
  }
  
  sliderChange(number){
    this.props.onSliderDataPass(number)
  }
   
  render() {
    const marks = {
      1953: 1953,
      2018: 2018
    }
    console.log("fff", this.props.defaultValue)
    // if(this.props.defaultValue == undefined){
    //   var def = [1965,2004]

    // }else{
    //   console.log("dfdsf", this.props.defaultValue)
    //   // var temp = this.props.defaultValue.years;
    //   var def = [1965,2004];
    //   // var def = [temp[0], temp[1]]
    // }

     return (
       
       
      <div>
        <Slider range marks={marks} defaultValue={this.props.defaultValue} max={2018} min={1953} tooltipVisible onChange={this.sliderChange} />
        </div>
    );
  }
}

export default YearsSlider;