// import '../App.css';
// import 'rc-slider/assets/index.css';
// import 'rc-tooltip/assets/bootstrap.css';
// import React, { Component } from 'react';
// import ReactDOM from 'react-dom';
//  import Tooltip from 'rc-tooltip';
//  import Slider from 'rc-slider';
 
// const createSliderWithTooltip = Slider.createSliderWithTooltip;
// const Range = createSliderWithTooltip(Slider.Range);
// const Handle = Slider.Handle;

// const handle = (props) => {
//   const { value, dragging, index, ...restProps } = props;
//   return (
//     <Tooltip
//       prefixCls="rc-slider-tooltip"
//       overlay={value}
//       visible={dragging}
//       placement="top"
//       key={index}
//     >
//       <Handle value={value} {...restProps} />
//     </Tooltip>
//   );
// };

// const wrapperStyle = {  margin: 15 };
// class MySlider extends Component
// {

//   constructor(props){
//     super(props);
//   //   this.state = {
//   //     value4: {
//   //      min: 1953,
//   //      max: 2018,
//   //   },
//   // };
//    this.sliderChange = this.sliderChange.bind(this);
//   }

//   sliderChange(event){
//     this.props.onSliderDataPass(event);
//   }
  
//   render()
//   {
//     return(
//       <div >
//          <div style={wrapperStyle}  id="mygreen">
//           <h3>Year</h3>
//           <Range min={1953} max={2018} defaultValue={[2000, 2010]} tipFormatter={value => `${value}`} onChange={this.sliderChange}/>
//         </div>
//       </div>
//       );
//     }
//   }

//   // render() {
//   //   return (
//   //     <Paper
//   //     value="183"
//   //     max="255"
//   //     secondary-progress="200"
//   //     editable>
//   //   </Paper>
//   //   );
//   // }

//   // render() {
//   //   return (
//   //     <form className="form">
//   //       <InputRange
//   //         maxValue={2018}
//   //         minValue={1953}
//   //         value={this.state.value4}
//   //         onChange={value => this.setState({ value4: value })}
//   //         onChangeComplete={value => console.log(value)} />
//   //     </form>
//   //   );
//   // }

// //}


//   export default MySlider;

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