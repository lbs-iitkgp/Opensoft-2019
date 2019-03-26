import React from "react";
import { withStyles } from "@material-ui/core/styles";
import Chip from "@material-ui/core/Chip";


const styles = theme => ({
  root: {
    display: "flex",
    justifyContent: "center",
    flexWrap: "wrap",
    size : 400
  },
  chip: {
    margin: theme.spacing.unit
  }
});


function Chips(props) {
  const { classes } = props;
  return (
    <div className={classes.root}>
     
       <Chip
        label={props.actName}
        className={classes.chip}
        color="primary"
      />
      
    </div>
  );
}

export default withStyles(styles)(Chips);
