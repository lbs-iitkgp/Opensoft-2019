import React from 'react';
import { makeStyles } from '@material-ui/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';

function TabContainer(props) {
  return (
    <Typography component="div" style={{ padding: 8 * 3 }}>
      {props.children}
    </Typography>
  );
}


const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
}));

function SimpleTabs() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  function handleChange(event, newValue) {
    setValue(newValue);
  }

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Tabs value={value} onChange={handleChange}>
          <Tab label={props.labelOne} />
          <Tab label={props.labelTwo} />
        </Tabs>
      </AppBar>
      {value === 0 && <TabContainer>{props.itemOne}</TabContainer>}
      {value === 1 && <TabContainer>{props.itemTwo}</TabContainer>}
     </div>
  );
}

export default SimpleTabs;
