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
// const name = <a href="saas">Dibya</a>
class AdvFilter extends React.Component {
  constructor(props){
      super(props);
      this.state = {
        columns: ['Date', 'Indlaw ID','Judgement', "Title"],
        data: [
          ["name", 'Minneapolis', 30, '$100,000'],
          ['Aiden Lloyd', 'Dallas', 55, '$200,000'],
          ['Jaden Collin', 'Santa Ana', 27, '$500,000'],
          ['Franky Rees', 'St. Petersburg', 22, '$50,000'],
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
      // var self = this;
       
      console.log("idhar", this.props);
      axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/`+this.props.myurl)
        .then((response) => {
          console.log(response);
          return response.data.map((ele) => {
            return Object.entries(ele).map((ind) => ind[1])
          })
        })
        .then((sanit_pre)=> {
          console.log(sanit_pre); 
          // var to_have = []
          // for (let index = 0; index < sanit_pre.length; index++) {
          //   const element = sanit_pre[index];
          //   let temp = [];
          //   for (let index2 = 0; index2 < 8; index2++) {
          let topass = [1,0,1,1,1,0,0,0];
          return sanit_pre.map( (case_e,id) =>  case_e.filter((ele, index) => topass[index]))
          //     if(topass[index2])
          //      temp.push(element[index][index2]) 
          //   }
          //   to_have.push(temp);  
          // }
          // return to_have;
          // san
          
        })
        .then((sanit) => {
          // handle success
          console.log(sanit)  
          this.setState({
            data: sanit
            // columns : Object.keys(response.data[0])
          })
          // console.log(this.state.data);
          // console.log(this.state.columns);
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
      // rowsPerPage: data.rowsPerPage,
      // page: data.pagenumber,
      // onChangePage : this.onChangePages,
      // onChangeRowsPerPage : this.onChangeRowsPerPages,
      // onFilterChange : this.onFilterChanges,
      // onColumnSortChange : this.onColumnSortChanges,
      rowsPerPageOptions : [5,10,15]
    };
    return (
      <MUIDataTable
        title="Case list"
        data={data}
        columns={columns}
        // options={options}
      />
    );
  }
}

export default AdvFilter;