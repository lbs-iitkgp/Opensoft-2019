import React from 'react';
import { makeStyles } from '@material-ui/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import ActsAccord from './actsaccord.js'
import AdvTable from './advtable.js'

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
          <Tab label="Sections" />
          <Tab label="Cases" />
        </Tabs>
      </AppBar>
      {value === 0 && <TabContainer><ActsAccord /></TabContainer>}
      {value === 1 && <TabContainer><AdvTable /></TabContainer>}
     </div>
  );
}

export default SimpleTabs;
