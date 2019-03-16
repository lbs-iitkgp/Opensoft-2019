import React, { Component } from 'react';
import { MDBCol, MDBFormInline, MDBBtn } from "mdbreact";

import { render } from "react-dom";
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import FormLabel from '@material-ui/core/FormLabel';
//import starWarsNames from "starwars-names";

import MultiChipSelect from "./MultiChipSelect";


class Category extends Component{
  //mine  below
  constructor(props){
       super(props);
       this.passData = this.passData.bind(this); 
  // this.handleChange= this.handleChange.bind(this);
  // this.addSelectedItem= this.addSelectedItem.bind(this);
  // this.removeSelectedItem=this.removeSelectedItem.bind(this);
  // this.handleChangeInput=this.handleChangeInput.bind(this);
    }
    
     passData(event){
       var searchedCat = event.target.value;
       this.props.onCategoryDataPass(searchedCat);
    }
//mine above

    // allItems = starWarsNames
    // .random(7)
    // .map(s => ({ name: s, id: s.toLowerCase() }));

  //   allItems=[{name:'kau',id:'k'},{name:'sau',id:'s'},{name:'nau',id:'n'},{name:'mau',id:'m'}];
  // state = {
  //   items: this.allItems,
  //   selectedItem: []
  // };

  // handleChange = selectedItem => {
  //   if (this.state.selectedItem.includes(selectedItem)) {
  //     this.removeSelectedItem(selectedItem);
  //   } else {
  //     this.addSelectedItem(selectedItem);
  //   }
  // };

  // addSelectedItem(item) {
  //   this.setState(({ selectedItem, items }) => ({
  //     inputValue: "",
  //     selectedItem: [...selectedItem, item],
  //     items: items.filter(i => i.name !== item)
  //   }));
  // }

  // removeSelectedItem = item => {
  //   this.setState(({ selectedItem, items }) => ({
  //     inputValue: "",
  //     selectedItem: selectedItem.filter(i => i !== item),
  //     items: [...items, { name: item, id: item.toLowerCase() }]
  //   }));
  // };

  // handleChangeInput = inputVal => {
  //   const t = inputVal.split(",");
  //   if (JSON.stringify(t) !== JSON.stringify(this.state.selectedItem)) {
  //     this.setState({ inputValue: inputVal });
  //   }
  // };

     
      render(){
        // const { selectedItem, items } = this.state;
        // return (
        //   <FormGroup>
        //     <FormControl>
        //       <FormLabel>Find a Star Wars character</FormLabel>
        //       <MultiChipSelect
        //         onInputValueChange={this.handleChangeInput}
        //         inputValue={this.state.inputValue}
        //         availableItems={items}
        //         selectedItem={selectedItem}
        //         onChange={this.handleChange}
        //         onRemoveItem={this.removeSelectedItem}
        //       />
        //     </FormControl>
        //   </FormGroup>
        // );
        const wrapperStyle = {  margin: 20 };

      return (
        <MDBCol md="12" style={wrapperStyle}>
          <h3> Category </h3>
          <MDBFormInline className="md-form mr-auto mb-4">
              <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" id="category" onChange={this.passData} defaultValue = ''  />
          </MDBFormInline>
        </MDBCol>
      );
     }
    }
   
    export default Category;