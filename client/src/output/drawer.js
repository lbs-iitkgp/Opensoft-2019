import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import Button from '@material-ui/core/Button';
import YearsSlider from '../components/slider.js'
import SearchBar from '../components/query.js';
import Category from '../components/category.js';
import Judges from '../components/judges.js';
import Acts from '../components/acts.js';
import '../App.css'

const drawerWidth = 240;

var Results={
    query : '',
    years : [],
    category : '',
    judgeName : '',
    selectedActs :[]
  }

const styles = theme => ({
  root: {
    display: 'flex',
  },
  appBar: {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth,
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: 450,
  },
  toolbar: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
    padding: theme.spacing.unit * 3,
  },
});

function updateResultJudge(JudgeRes){
    Results.judgeName = JudgeRes; 
  }
  
function  updateResultCat(catRes){
    Results.category = catRes;
  }
   
function  updateResultQuery(queryRes){
    Results.query=queryRes
    }
  
function  updateResSelectedAct(selectedActPass){
    Results.selectedActs = selectedActPass
  }
  
function  updateSliderResult(sliderPass){
    Results.years  = sliderPass.slice(0,2)
    }

function  printResults(){
    console.log(Results.query);
    console.log(Results.years[0], Results.years[1]);
    console.log(Results.category);
    console.log(Results.judgeName);
    console.log(Results.selectedActs);
  }

function PermanentDrawerLeft(props) {
  const { classes } = props;

  return (
    <div className={classes.root} >
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
        anchor="left"
      >
      <div id='drawer1'>
      <h2>Search</h2>
        <SearchBar OnQueryPass={updateResultQuery }   />
        <h2>Years</h2>
        <br />
        <YearsSlider onSliderDataPass={  updateSliderResult }  />
        <Category onCategoryDataPass={  updateResultCat }  />
        <Judges  onJudgeNamePass={  updateResultJudge } /> 
        <br />
        <h2>Acts</h2>
        <Acts  onSelectedActsPass={  updateResSelectedAct } />
        <br />
        <div className='searchButton'>
            <Button variant="contained" color="primary" onClick={  printResults } style={{width:'130px',height:'50px'}}>
                Update
            </Button>
        </div>
      </div> 
        </Drawer>
           
     </div>
  );
}



export default withStyles(styles)(PermanentDrawerLeft);
