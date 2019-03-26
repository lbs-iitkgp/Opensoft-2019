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
  
     return (
      <div>
        <Slider range marks={marks} defaultValue={[1965, 2004]} max={2018} min={1953} tooltipVisible onChange={this.sliderChange} />
        </div>
    );
  }
}

export default YearsSlider;