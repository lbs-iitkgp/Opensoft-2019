import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    fontSize: 30
  },
  body: {
    fontSize: 25
  }
}))(TableCell);

const styles = theme => ({
  root: {
    width: "100%",
    marginTop: theme.spacing.unit * 1,
    overflowX: "auto"
  },
  table: {
    minWidth: 1000
  }
});

let id = 0;
function createData(list, judgement, judgename, actsCited, category, date) {
  id += 1;
  return { id, list, judgement, judgename, actsCited, category, date };
}

const rows = [
  createData(
    "url/snippet",
    "appeal allowed",
    "mahajan",
    "indian stmap act",
    "criminal",
    "12-12-12"
  ),
  createData(
    "url/snippet",
    "appeal allowed",
    "mahajan",
    "indian stmap act",
    "criminal",
    "12-12-12"
  ),
  createData(
    "url/snippet",
    "appeal allowed",
    "mahajan",
    "indian stmap act",
    "criminal",
    "12-12-12"
  ),
  createData(
    "url/snippet",
    "appeal allowed",
    "mahajan",
    "indian stmap act",
    "criminal",
    "12-12-12"
  )
];

function CustomizedTable(props) {
  const { classes } = props;

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <CustomTableCell align="left">List Of Cases</CustomTableCell>
            <CustomTableCell align="right">Judgement</CustomTableCell>
            <CustomTableCell align="right">Judge</CustomTableCell>
            <CustomTableCell align="right">Acts Cited</CustomTableCell>
            <CustomTableCell align="right">Case Category</CustomTableCell>
            <CustomTableCell align="right">Date</CustomTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow className={classes.row} key={row.id}>
              <CustomTableCell align="left">{row.list}</CustomTableCell>
              <CustomTableCell align="right">{row.judgement}</CustomTableCell>
              <CustomTableCell align="right">{row.judgename}</CustomTableCell>
              <CustomTableCell align="right">{row.actsCited}</CustomTableCell>
              <CustomTableCell align="right">{row.category}</CustomTableCell>
              <CustomTableCell align="right">{row.date}</CustomTableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}

export default withStyles(styles)(CustomizedTable);
