import React, { Component } from 'react';
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import starWarsNames from "starwars-names";
import MultiChipSelect from "./MultiChipSelect.js";



class Category extends Component{
  constructor(props){
    super(props);
  this.handleChange= this.handleChange.bind(this);
  this.addSelectedItem= this.addSelectedItem.bind(this);
  this.removeSelectedItem=this.removeSelectedItem.bind(this);
  this.handleChangeInput=this.handleChangeInput.bind(this);
  this.passData = this.passData.bind(this);
  }
   
  passData(event){
    this.props.onCategoryDataPass(event);
  }

  allItems = starWarsNames
    .random(7)
    .map(s => ({ name: s, id: s.toLowerCase() }));

  state = {
    items: this.allItems,
    selectedItem: []
  };

  handleChange = selectedItem => {
    if (this.state.selectedItem.includes(selectedItem)) {
      this.removeSelectedItem(selectedItem);
    } else {
      this.addSelectedItem(selectedItem);
    }
   };

  addSelectedItem=item => {
    this.setState(({ selectedItem, items }) => ({
      inputValue: "",
      selectedItem: [...selectedItem, item],
      items: items.filter(i => i.name !== item)
    }));
  }

  removeSelectedItem = item => {
    this.setState(({ selectedItem, items }) => ({
      inputValue: "",
      selectedItem: selectedItem.filter(i => i !== item),
      items: [...items, { name: item, id: item.toLowerCase() }]
    }));
  };

  handleChangeInput = inputVal => {
    const t = inputVal.split(",");
    if (JSON.stringify(t) !== JSON.stringify(this.state.selectedItem)) {
      this.setState({ inputValue: inputVal });
   
    }
  }
     
      render() {
        const { selectedItem, items } = this.state
        return (
        // <MuiThemeProvider> 
          <FormGroup>
            <FormControl>
              <h3>Category</h3>
              <MultiChipSelect
                onInputValueChange={this.handleChangeInput}
                inputValue={this.state.inputValue}
                availableItems={items}
                 selectedItem={selectedItem}
                onChange={this.handleChange}
                onRemoveItem={this.removeSelectedItem}
                onInputValueChange={this.passData}
               />
            </FormControl>
          </FormGroup>
        //  </MuiThemeProvider> 
        );
      }
    }
   
    export default Category;