import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import "../App.css";
import Chips from '../chips.js'
import 'material-ui-icons'
import axios from 'axios';

function createData(listData, index) {
  
  var type = listData.type;
  var name = listData.name;
  var url = listData.url;
  return { index, type, name, url } ;
  }

// var cardsData = [
//   {
//     "type" : 'KEYWORD',
//     "name" : 'Criminal',
//     "url" : '#',
    
//   }].map((ele, ind) => createData(ele, ind) );  


class Demo extends Component{
  constructor(...props){
    super(...props);
  this.state = {
    minWidth  : 300,
    color : '',
    fontSize: 14,
    marginBottom: 12,
    padding : 10,
    loaded : false,
    margin :10,
    cardsColor :[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    cardsData : ''
  }

      this.removeCard = this.removeCard.bind(this);
      this.printPresentCards = this.printPresentCards.bind(this);
      }

      printPresentCards(){
              }


      callAxios(data){
        axios.get(`${process.env.REACT_APP_BACKEND_ORIGIN}/search/cards?query=${data}`)
        .then((response) => {
              console.log("cardss",response.data);
            var p = response.data.map(ele => {
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
            this.props.activate();
          })
          .catch(function (error) {
            console.log(error);
          });
      }

      componentDidMount(){
        this.callAxios(this.props.cardQuery);
      }

      componentDidUpdate()
      {
        this.printPresentCards();
      }

      removeCard(id){
          let removeC = () => {
              const localId = id;
              var content = document.getElementById(localId);
              content.remove();
              var arr = this.state.cardsColor;
              arr[localId] = 0;
              this.setState({
                cardsColor : arr
              })
          }
          //this.printPresentCards();
          return removeC;
      }

      generateCards(cardsData){
        return (
          <div id="content" className="flex-container">
            {cardsData.map( ele => (
              <Card  className="card" style={{ minWidth : this.state.minWidth }} id={ele.index}  >
                <div id='chipCross'><Chips title={ele.type} /><i class="material-icons md-48" onClick={this.removeCard(ele.index)} >highlight_off</i></div>
                <div id="cardType">
                  <b><h3><a href={ele.url}>{ele.name}</a> </h3></b>
                </div>
              </Card>
            ))}
          </div>
          );
      }

      render() {
              return (
                 (this.state.loaded) ? this.generateCards(this.state.cardsData) : '' 
              );
          }
          

          }

          export default Demo;