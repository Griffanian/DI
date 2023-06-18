import React from 'react'
import quotes from '../QuotesDatabase'
import '../css/Quote.css';

class Quote extends React.Component {
    constructor(){
        super()
        this.state={
            quoteObj : null,
            numsArr: [],
            currentIndex : 0,
            color : '',
        }
    }
    quotes = quotes
    genList = async () => {
        const array = Array(94).fill(1).map((n, i) => n + i - 1)
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
          }
        this.setState({numsArr:array}, () => {
            this.updateQoute();
          });
    }

    updateQoute = () => {
        const index = this.state.currentIndex
        const array = this.state.numsArr
        const obj = this.quotes[array[index]]
        this.setState({
            quoteObj: obj,
            currentIndex:this.state.currentIndex+1
        }, () => {
            this.setRandomColor();
        });
    }

    componentDidMount = () => {
        this.genList() 
    }
    setRandomColor = () => {
        const r = Math.floor(Math.random() * 150);
        const g = Math.floor(Math.random() * 150);
        const b = Math.floor(Math.random() * 150);
        this.setState({color:`rgb(${r}, ${g}, ${b})`})
      };
    render(){
        if (this.state.quoteObj){
            return(
                <div id="container" style={{'backgroundColor':this.state.color}}>
                    <div id="box" style={{'color':this.state.color}}>
                        <h1>{this.state.quoteObj.quote}</h1>
                        <h5>-{this.state.quoteObj.author?this.state.quoteObj.author:"Unknown"}-</h5>
                        <button style={{'backgroundColor':this.state.color}} id="newQoute" onClick={this.updateQoute}>New qoute</button>
                    </div>
                </div>
            )
        }
    }
}
export default Quote