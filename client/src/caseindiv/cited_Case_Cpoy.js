import React,{Component} from 'react';
import PropTypes from 'prop-types';
import SwipeableViews from 'react-swipeable-views';
import { makeStyles } from '@material-ui/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import '../App.css'
import axios from 'axios'

function TabContainer({ children, dir }) {
  return (
    <Typography component="div" dir={dir} style={{ padding: 8 * 3 }}>
      {children}
    </Typography>
  );
}


const useStyles = makeStyles(theme => ({
  root: {
    //backgroundColor: theme.palette.background.paper,
    width: 500,
  },
}));

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


class FullWidthTabs2 extends Component{
  constructor(props){
    super(props);
    this.state = {
      result : [],
      value : 0,
      setvalue : 0,
      has_loaded: false
    }
 
    this.handleChange = this.handleChange.bind(this);
    this.handleChangeIndex = this.handleChangeIndex.bind(this);
    this.makeActUrl = this.makeActUrl.bind(this);
    this.makeCaseUrl  = this.makeActUrl.bind(this);
    this.updateCases = this.updateCases.bind(this);
  }

  componentDidMount(){
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}${this.props.myurl}`)
      .then(response => {
        console.log(new Array(response.data));
        this.setState({ result: new Array(response.data), has_loaded: true });

      })
      .catch(function (error) {
        // handle error
        console.log('error is ' + error);
      })
      .then(function () {
        // always executed
      });
  }

  updateCases(){
  }

  handleChange(event, newValue) {
    //alert(newValue);
    this.setState({
      value : newValue
    });
  }

  handleChangeIndex(index) {
    this.setState({
      value: index
    });
  }

  makeCaseUrl(ele) {
  return `${process.env.REACT_APP_FRONTEND_ORIGIN}/modal/${ele}`;
  }

  makeActUrl(ele) {
    return `${process.env.REACT_APP_FRONTEND_ORIGIN}/act/${ele}`;
  }

  formcards(){
    Acts = this.state.result[0].cited_acts;
    citedIn = this.state.result[0].cited_by_cases;
    citedOut = this.state.result[0].cited_cases;
    console.log(citedIn[0].name);
    return (<div>
    <TabContainer >
      <ul>
        {citedIn.map((index, ele) => (<li><a href={this.makeCaseUrl(1)}>{ele.name}</a></li>))}
      </ul>
    </TabContainer>
      <TabContainer >
        <ul>
          {citedOut.map((index, ele) => (<li><a href={this.makeCaseUrl(1)}>{ele.name}</a></li>))}
        </ul>
      </TabContainer>
      <TabContainer >
        <ul>
          {Acts.map((index, ele) => (<li><a href={this.makeActUrl(1)}>{ele.name}</a></li>))}
        </ul>
      </TabContainer>
      </div>)
  }

  render() {
    
    //const classes = useStyles();
    console.log("Aadi",this.state.result);
    
    console.log("render",this.state.result);
    return (
      <div >
        <AppBar position="static" color="default">
          <Tabs
            value={this.state.value}
            onChange={this.handleChange}
            indicatorColor="primary"
            textColor="primary"
            variant={null}
          >
            <Tab label="cited in" />
            <Tab label="cited by" />
            <Tab label="Acts" />
          </Tabs>
        </AppBar>
        <SwipeableViews
          axis='x'
          index={this.state.value}
          onChangeIndex={this.handleChangeIndex}
        >
          { this.state.has_loaded ? this.formcards() : '' }
        </SwipeableViews>
      </div>
    );
  }
}

export default FullWidthTabs2;