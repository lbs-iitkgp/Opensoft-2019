import React from 'react';
import PropTypes from 'prop-types';
import SwipeableViews from 'react-swipeable-views';
import { makeStyles} from '@material-ui/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import '../App.css'

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

function createData(data,index){
  return{index,data}
}

var citedIn =[
  'case-1',
  'case-2',
  'case-1',
  'case-2',
  'case-1',
  'case-2',
].map((ele, ind) => createData(ele, ind) );

var citedOut =[
  'case-1',
  'case-2',
  'case-1',
  'ca-2',
  'case-1',
  'case-2',
].map((ele, ind) => createData(ele, ind) );

var Acts =[
  'case-1',
  'case-2',
  'cas1',
  'case-2',
  'case-1',
  'case-2',
].map((ele, ind) => createData(ele, ind) );

function FullWidthTabs() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  function handleChange(event, newValue) {
    setValue(newValue);
  }

  function handleChangeIndex(index) {
    setValue(index);
  }

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
            <a href="#">{citedIn.map(ele => (<li>{ele.data}</li>))}</a>
          </ul>
        </TabContainer>
        <TabContainer >
        <ul>
           <a href="#">{citedOut.map(ele => (<li>{ele.data}</li>))}</a>
         </ul>
      </TabContainer>
      <TabContainer >
         <ul>
         <a href="#">{Acts.map(ele => (<li>{ele.data}</li>))}</a>
         </ul>
     </TabContainer>
       </SwipeableViews>
    </div>
  );
}

export default FullWidthTabs;
