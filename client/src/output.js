import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import "./App.css";

const styles = {
  card: {
    minWidth: 240
     },
  title: {
    fontSize: 14
  },
  pos: {
    marginBottom: 12,
    padding : 10,
    margin :10
  }
};

let id = 0;
function createData(Case, Judgement, Judge, Act, Category, Date) {
  id += 1;
  return { id, Case, Judgement, Judge, Act, Category, Date };
}

const list = [
  createData(
    "mycase",
    "appeal",
    "mahajan",
    "indian stamp act",
    "criminal",
    "12-12-12"
  ),
  createData(
    "mycase",
    "appeal",
    "mahajan",
    "indian stamp act",
    "criminal",
    "12-12-12"
  )
];

function SimpleCard(props) {
  const { classes } = props;
   return (
    <div id="content" className="flex-container">
      {list.map(ele => (
        <Card className={classes.card} id="card">
          <div id="case"><h2 href="#"> {ele.Case}</h2></div>
          <div id="judgement">
            <b>Judgement:</b> {ele.Judgement}
          </div>
          <div id="judge">
            <b>Judge:</b> {ele.Judge}
          </div>
          <div id="act">
            <b>Act cited:</b> {ele.Act}
          </div>
          <div id="category">
            <b>Category : </b> {ele.Category}
          </div>
          <div id="date">
            <b>Date :</b> {ele.Date}
          </div>
          <br /><br />
        </Card>
      ))}
    </div>
  );
}

export default withStyles(styles)(SimpleCard);
