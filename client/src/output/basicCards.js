  import React, { Component } from "react";
  import Card from "@material-ui/core/Card";
  import "../App.css";
  import Switches from '../switches.js'
  import Chips from '../chips.js'
  import axios from 'axios'


  function createData(listData, index) {
    var type = listData.type
    var name = listData.name
    var url = listData.url
    
    return { index, type,name, url } ;
    }

  var cardsData = [
    {
      "name" : "JUDGE",
      "index" : "H. R. Khanna",
      "type"  : "#",
      "url"   : '1'
    }
  ,
  {
    "name" : "JUDGE",
      "index" : "H. R. Khanna",
      "type"  : "",
      "url"   : ''
  }].map((ele, ind) => createData(ele, ind) );  


  class Demo extends Component{
    constructor(...props){
      super(...props);
    this.state = {
      minWidth  : 240,
      color : '',
      fontSize: 14,
      marginBottom: 12,
      padding : 10,
      margin :10,
      cardsData: [{}],
      cardsColor : {},
      identifier : [],
      loaded : true
    }
  this.handleToggle = this.handleToggle.bind(this);
  }

  

  handleToggle(colorDecider, index){
    index = index.toLowerCase()
     var localcardsColor = this.state.cardsColor;
    if(!colorDecider)
    {
        console.log(index);
        localcardsColor[index] = '';       
    }
    else if(colorDecider) 
    {
      console.log(index);
        localcardsColor[index] = '#c6c6c6';
    }
    this.setState({
      cardsColor : localcardsColor
    })
   // this.printActiveCardsInfo();
   var activecards = new Array();

    console.log(this.state.cardsColor)
    Object.keys(this.state.cardsColor).map(e => {
      if (this.state.cardsColor[e.toLowerCase()] == '') {
        activecards.push(e.toLowerCase());
      }
    })
    console.log("Active:", activecards);
  //  for(var i =0;i<this.state.cardsData.length;i++){
  //    if(this.state.cardsColor[i]=='')
  //       activecards.push(this.state.cardsData[i]);}
  //     else
  //      {
  //        console.log(this.state.cardsColor[i] )
  //         continue
          
  //      }  
  //  }
  // console.log(this.state.cardsData.length,"lenth")

   console.log("func working",activecards)
   axios.post(`${process.env.REACT_APP_BACKEND_ORIGIN}/search/basic/stage_2`, {
              active_cards : activecards
    })
      .then(function (response) {
        console.log(response);
              
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  callAxios(data){
    axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/search/cards?query=${data}`)
    .then((response) => {
          console.log("cardss",response.data);
         var p = response.data.map(ele => {
          this.state.cardsColor[ele.result_type+"_"+ele.serial] = ''
          return ({"name" : ele.name.length > 35 ? ele.name.slice(0,35)+"..." : ele.name, "index": ele.serial, "type": ele.result_type.toUpperCase() }  )
          });
         console.log(p);
         return p;
      })
      .then((sanitisedResponse) => {
        this.setState({
          cardsData :sanitisedResponse,
          loaded : true
        })
        console.log("this.state.cardsData------------ " ,this.state.cardsData)

      })
      .catch(function (error) {
        console.log(error);
      });
  }

  componentDidMount(){
     //filter function
    ///  var cardsdata = this.state.cardsData
         this.callAxios(this.props.parState);
  }

  urlTo(id){
    return `keywords/${id}`
  }

  generateCards(Cdata){
    console.log(Cdata)
    return Cdata.map( ele   => (
      <Card  className="card" style={{ color : this.state.cardsColor[ele.index], minWidth: this.state.minWidth }} id={ele.index} >
        <div id="case"><div className="chip"><Chips title={ele.type} /></div><Switches id={ele.type+"_"+ele.index} OnPassChecked={this.handleToggle}  /></div>
        <div >
          <a href={this.urlTo(ele.index)}><b>{ele.name}</b></a>
        </div>
      </Card>
    ))
  }


  
  render() {
      return (
            <div id="content" className="flex-container">
              {this.state.loaded ? this.generateCards(this.state.cardsData) : '' }
            </div>
            );
      }
      }

      export default Demo;