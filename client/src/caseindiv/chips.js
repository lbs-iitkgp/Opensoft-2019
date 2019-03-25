import React from "react";
import { withStyles } from "@material-ui/core/styles";
import Chip from "@material-ui/core/Chip";
import Tooltip from '@material-ui/core/Tooltip';

const longText = `
Aliquam eget finibus ante, non facilisis lectus. Sed vitae dignissim est, vel aliquam tellus. 
Praesent non nunc mollis, fermentum neque at, semper arcu. 
Nullam eget est sed sem iaculis gravida eget vitae justo. 
`;

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
     <Tooltip title={longText}> 
       <Chip
        label={props.actName}
        className={classes.chip}
        color="primary"
      />
     </Tooltip> 
    </div>
  );
}

export default withStyles(styles)(Chips);
