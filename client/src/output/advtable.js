import React from 'react';
import MUIDataTable from 'mui-datatables';
/*
  It uses npm mui-datatables. It's easy to use, you just describe columns and data collection.
  Checkout full documentation here :
  https://github.com/gregnb/mui-datatables/blob/master/README.md
*/

// var options = {
//   filters : '',
//   rowsPerPage : 10,
//   pagenumber : 0,
//   sortColumn : []
// }

class AdvFilter extends React.Component {
  constructor(props){
      super(props);
      // this.state = {
      //   columns: ['MyName', 'Title', 'Location', 'Age', 'Salary',1,2,3],
      //   data: [
      //     ['Gabby George', 'Business Analyst', 'Minneapolis', 30, '$100,000',1,2,3],
      //   ]
      // }
      // console.log("sfsfsef")
      // console.log(this.props.data, "dfeg")
      this.state = {
        columns: ['Date', 'Indlaw ID', 'Judgement', 'Title', 'Summary'],
        res: this.props.data  
      }
      // this.onChangePages = this.onChangePages.bind(this);
      // this.onChangeRowsPerPages = this.onChangeRowsPerPages.bind(this);
      // this.onFilterChanges = this.onFilterChanges.bind(this);
      // this.onColumnSortChanges = this.onColumnSortChanges.bind(this);
    }

  componentDidMount(){
    console.log(this.props,"asdsad")
    // this.callAxios()
    // this.setState({
    //   res: this.props.data
    // })
  }    

    // onColumnSortChanges(changedColumn,direction){
    //   data.sortColumn = {column : changedColumn, order : direction};
    //   console.log(data.sortColumn);
    // }

    // onChangePages(number){
    //   data.pagenumber = number;
    //   console.log('Page changed',data);
    // }

    // onChangeRowsPerPages(number){
    //   data.rowsPerPage = number;
    //   console.log("Rows per page changed",data);
    // }

    // onFilterChanges(changedColumn, filterList)
    // {
    //   data.filters = filterList;
    //   console.log("Filters Changed", data, changedColumn);
    // }

  render() {
    const { columns, res } = this.state;
    const options = {
      filterType: 'multiselect',
      responsive: 'stacked',
      print: true,
      // rowsPerPage: data.rowsPerPage,
      // page: data.pagenumber,
      // onChangePage : this.onChangePages,
      // onChangeRowsPerPage : this.onChangeRowsPerPages,
      // onFilterChange : this.onFilterChanges,
      // onColumnSortChange : this.onColumnSortChanges,
      // rowsPerPageOptions : [10,15]
    };
    return (
      <MUIDataTable
        title="Case list"
        data={res}
        columns={columns}
        options={options}
      />
    );
  }
}

export default AdvFilter;