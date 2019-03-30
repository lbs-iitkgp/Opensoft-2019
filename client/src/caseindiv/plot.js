import React from 'react';
import { AreaClosed, Line, Bar } from '@vx/shape';
import { appleStock } from '@vx/mock-data';
import { curveMonotoneX } from '@vx/curve';
import { ParentSize } from '@vx/responsive';
import { GridRows, GridColumns } from '@vx/grid';
import { scaleTime, scaleLinear } from '@vx/scale';
import { withTooltip, Tooltip } from '@vx/tooltip';
import { localPoint } from '@vx/event';
import { bisector } from 'd3-array';
import { timeFormat } from 'd3-time-format';
import axios from 'axios'
  
// const stock = appleStock.slice(800);
var stock = {
  1934: 19,
  1936: 7,
  1940: 42,
  1943: 5
}
//console.log(stock);
//console.log('stock minimize' + stock.slice(10))

// util
const formatDate = timeFormat(" %y");
const min = (arr, fn) => Math.min(...arr.map(fn));
const max = (arr, fn) => Math.max(...arr.map(fn));
const extent = (arr, fn) => [min(arr, fn), max(arr, fn)];

// var data = []

// for (var i = 100 - 1; i >= 0; i--) {
//   data.push({ "index": i, "val": i*2})
// }

function convertToProperData(stock){
  return Object.keys(stock).map((k) =>
    ({ "date": k, "close": stock[k]})
  )
}
//stock = convertToProperData(stock)

//console.log(convertToProperData("AadiOutside",stock));

// function xStock (d){
//   console.log()
//   return d.index
// }
const xStock = d => d.date;
const yStock = d => d.close;
const bisectDate = bisector(d => d.date).left;

class Area extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stock : convertToProperData(stock)
    }
    this.handleTooltip = this.handleTooltip.bind(this);
  }
  handleTooltip({ event, data, xStock, xScale, yScale }) {
    const { showTooltip } = this.props;
    const { x } = localPoint(event);
    const x0 = xScale.invert(x);
    const index = bisectDate(data, x0, 1);
    const d0 = data[index - 1];
    const d1 = data[index];
    let d = d0;
    if (d1 && d1.date) {
      d = x0 - xStock(d0.date) > xStock(d1.date) - x0 ? d1 : d0;
    }
    showTooltip({
      tooltipData: d,
      tooltipLeft: x,
      tooltipTop: yScale(d.close)
    });
  }
  
  componentWillMount(){
    var self = this;
    // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}${self.props.myurl}`)
      .then(function (response) {
        self.setState({ stock: convertToProperData(response.data) })
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
    const {
      width=500,
      height=500,
      margin= { top: 20, bottom: 20, left: 20, right: 20 },
      hideTooltip,
      tooltipData,
      tooltipTop,
      tooltipLeft,
      events
    } = this.props;
    if (width < 10) return null;

    // bounds
    const xMax = width - margin.left - margin.right;
    const yMax = height - margin.top - margin.bottom;


    // scales
    const xScale = scaleTime({
      range: [0, xMax],        
      domain: extent(this.state.stock, xStock)
    });
    const yScale = scaleLinear({
      range: [yMax, 0],
      domain: [0, max(this.state.stock, yStock) ],
      nice: true
    });
 
    //console.log('x axis is')

    return (
      <div>
        <svg ref={s => (this.svg = s)} width={width} height={height}>
          <rect x={0} y={0} width={width} height={height} fill="#32deaa" rx={14} />
          <defs>
            <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#FFFFFF" stopOpacity={1} />
              <stop offset="100%" stopColor="#FFFFFF" stopOpacity={0.2} />
            </linearGradient>
          </defs>
          <GridRows
            lineStyle={{ pointerEvents: 'none' }}
            scale={yScale}
            width={xMax}
            strokeDasharray="2,2"
            stroke="rgba(255,255,255,0.3)"
          />
          <GridColumns
            lineStyle={{ pointerEvents: 'none' }}
            scale={xScale}
            height={yMax}
            strokeDasharray="2,2"
            stroke="rgba(255,255,255,0.3)"
          />
          <AreaClosed
            data={this.state.stock}
            x={d => xScale(xStock(d))}
            y={d => yScale(yStock(d))}
            yScale={yScale}
            strokeWidth={1}
            stroke={'url(#gradient)'}
            fill={'url(#gradient)'}
            curve={curveMonotoneX}
          />
          <Bar
            x={0}
            y={0}
            width={width}
            height={height}
            fill="transparent"
            rx={14}
            data={this.state.stock}
            onTouchStart={event =>
              this.handleTooltip({
                event,
                xStock,
                xScale,
                yScale,
                data: this.state.stock
              })
            }
            onTouchMove={event =>
              this.handleTooltip({
                event,
                xStock,
                xScale,
                yScale,
                data: this.state.stock
              })
            }
            onMouseMove={event =>
              this.handleTooltip({
                event,
                xStock,
                xScale,
                yScale,
                data: this.state.stock
              })
            }
            onMouseLeave={event => hideTooltip()}
          />
          {tooltipData && (
            <g>
              <Line
                from={{ x: tooltipLeft, y: 0 }}
                to={{ x: tooltipLeft, y: yMax }}
                stroke="rgba(92, 119, 235, 1.000)"
                strokeWidth={2}
                style={{ pointerEvents: 'none' }}
                strokeDasharray="2,2"
              />
              <circle
                cx={tooltipLeft}
                cy={tooltipTop + 1}
                r={4}
                fill="black"
                fillOpacity={0.1}
                stroke="black"
                strokeOpacity={0.1}
                strokeWidth={2}
                style={{ pointerEvents: 'none' }}
              />
              <circle
                cx={tooltipLeft}
                cy={tooltipTop}
                r={4}
                fill="rgba(92, 119, 235, 1.000)"
                stroke="white"
                strokeWidth={2}
                style={{ pointerEvents: 'none' }}
              />
            </g>
          )}
        </svg>
        {tooltipData && (
          <div>
            <Tooltip
              top={tooltipTop - 12}
              left={tooltipLeft + 12}
              style={{
                backgroundColor: 'rgba(92, 119, 235, 1.000)',
                color: 'white'
              }}
            >
              {`${yStock(tooltipData)}`}
            </Tooltip>
            <Tooltip
              top={yMax - 14}
              left={tooltipLeft}
              style={{
                transform: 'translateX(-50%)'
              }}
            >
              {xStock(tooltipData)}
            </Tooltip>
          </div>
        )}
      </div>
    );
  }
}

export default withTooltip(Area);