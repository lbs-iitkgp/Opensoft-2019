import React from 'react';
import MUIDataTable from 'mui-datatables';
import axios from  'axios';
/*
  It uses npm mui-datatables. It's easy to use, you just describe columns and data collection.
  Checkout full documentation here :
  https://github.com/gregnb/mui-datatables/blob/master/README.md
*/

var data = {
  filters : '',
  rowsPerPage : 10,
  pagenumber : 0,
  sortColumn : []
}

class AdvFilter extends React.Component {
  constructor(props){
      super(props);
      this.state = {
        columns: ['MyName', 'Title', 'Location', 'Age', 'Salary'],
        data: [
          ['Aadi George', 'Business Analyst', 'Minneapolis', 30, '$100,000'],
          ['Aiden Lloyd', 'Business Consultant', 'Dallas', 55, '$200,000'],
          ['Jaden Collins', 'Attorney', 'Santa Ana', 27, '$500,000'],
          ['Franky Rees', 'Business Analyst', 'St. Petersburg', 22, '$50,000'],
          ]
      }
      this.onChangePages = this.onChangePages.bind(this);
      this.onChangeRowsPerPages = this.onChangeRowsPerPages.bind(this);
      this.onFilterChanges = this.onFilterChanges.bind(this);
      this.onColumnSortChanges = this.onColumnSortChanges.bind(this);
    }

    onColumnSortChanges(changedColumn,direction){
      data.sortColumn = {column : changedColumn, order : direction};
      console.log(data.sortColumn);
    }

    onChangePages(number){
      data.pagenumber = number;
      console.log('Page changed',data);
    }

    onChangeRowsPerPages(number){
      data.rowsPerPage = number;
      console.log("Rows per page changed",data);
    }

    onFilterChanges(changedColumn, filterList)
    {
      data.filters = filterList;
      console.log("Filters Changed", data, changedColumn);
    }

    componentWillMount() {
      //var id = this.props.match.params.id;
      var self = this;
      console.log(self.props);
      axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}`+self.props.myurl)
        .then(function (response) {
          // handle success
          self.setState({
            data: response.data,
            columns : Object.keys(response.data[0])
          })
          console.log(self.state.data);
          console.log(self.state.columns);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        })
        .then(function () {
          // always executed
        });

    }

  render() {
    const { columns, data } = this.state;
    const options = {
      filterType: 'multiselect',
      responsive: 'stacked',
      print: true,
      rowsPerPage: data.rowsPerPage,
      page: data.pagenumber,
      onChangePage : this.onChangePages,
      onChangeRowsPerPage : this.onChangeRowsPerPages,
      onFilterChange : this.onFilterChanges,
      onColumnSortChange : this.onColumnSortChanges,
      rowsPerPageOptions : [5,10,15]
    };
    return (
      <MUIDataTable
        title="Employee list"
        data={data}
        columns={columns}
        options={options}
      />
    );
  }
}

export default AdvFilter;