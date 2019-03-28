import React from 'react';
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

function bring_data(myurl){
  var result = {}
  // axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/judge/${id}`)
  axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}${myurl}`)
    .then(function (response) {
      result = response.data;
      return response.data;
      console.log("data", result);
    })
    .catch(function (error) {
      // handle error
      console.log('error is ' + error);
    })
    .then(function () {
      // always executed
    });
}

function FullWidthTabs({myurl}) {
  
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  function handleChange(event, newValue) {
    setValue(newValue);
  }

  function handleChangeIndex(index) {
    setValue(index);
  }

  function makeCaseUrl(ele){
    return `${process.env.REACT_APP_FRONTEND_ORIGIN}/modal/${ele}`;
  }

  function makeActUrl(ele) {
    return `${process.env.REACT_APP_FRONTEND_ORIGIN}/act/${ele}`;
  }

  var result = bring_data(myurl);
  console.log("Got data", result);

  return (
    <div className={classes.root}>
      <AppBar position="static" color="default">
        <Tabs
          value={value}
          onChange={handleChange}
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
        index={value}
        onChangeIndex={handleChangeIndex}
      >
        <TabContainer >
          <ul>
            {citedIn.map(ele => (<li><a href={makeCaseUrl(ele)}>{ele.data}</a></li>))}
          </ul>
        </TabContainer>
        <TabContainer >
          <ul>
            {citedOut.map(ele => (<li><a href={makeCaseUrl(ele)}>{ele.data}</a></li>))}
          </ul>
        </TabContainer>
        <TabContainer >
          <ul>
            {Acts.map(ele => (<li><a href={makeActUrl(ele)}>{ele.data}</a></li>))}
          </ul>
        </TabContainer>
      </SwipeableViews>
    </div>
  );
}

export default FullWidthTabs;