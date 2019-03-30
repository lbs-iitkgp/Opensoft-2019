import React,{Component} from 'react'
import CanvasJSReact from './canvasjs.react'
import axios from 'axios'

var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
var dummy =[
	{ y: '', label: '' },
	{ y: '', label: '' },
	{ y: '', label: '' },
	{ y: '', label: ''},
	{ y: '', label: '' }
]

class PieGraph extends Component {
	constructor(props){
		super(props)
		this.state={
			data_json : dummy
		}
	}
	
	componentWillMount(){
		// //var id = this.props.match.params.id;
		 // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
		 axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/${this.props.myurl}`)
		 .then((response) => {
			 console.log(response);
			return response.data;
		 })
		 .then((sanitised) => {
			this.setState({data_json : sanitised})
		 })
		 .catch(function (error) {
		   // handle error
		   console.log(error);
		 })
		 .then(function () {
		   // always executed
		 });   

			

	  }
	   
	
	
	render() {
		const options = {
			exportEnabled: true,
			animationEnabled: true,
			title: {
				text: "Graph"
			},
			data: [{
				type: "pie",
				startAngle: 75,
				toolTipContent: "<b>{label}</b>: {y}%",
				showInLegend: "true",
				legendText: "{label}",
				indexLabelFontSize: 16,
				indexLabel: "{label} - {y}%",
			dataPoints : Object.entries(this.state.data_json).map( (label, value) => {
				 return ({y : value ,label : label[0]})
			})	
			}]
		}
		return (
		<div>
			<CanvasJSChart options = {options}
				/* onRef={ref => this.chart = ref} */
			/>
			{/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
		</div>
		);
	}
}
export default PieGraph;                            