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

function handleDelete() {
  alert("You clicked the delete icon."); // eslint-disable-line no-alert
}

function handleClick() {
  alert("You clicked the Chip."); // eslint-disable-line no-alert
}

function Chips(props) {
  const { classes } = props;
  return (
    <div className={classes.root}>
      <Chip
        label={props.actName}
        onDelete={handleDelete}
        onClick={handleClick}
        className={classes.chip}
        color="primary"
      />
    </div>
  );
}

export default withStyles(styles)(Chips);
