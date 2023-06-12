import React from "react";

class ColorC extends React.Component {
    constructor(){
        super()
        this.state = {
            favoriteColor : "red"
        }
    }
    handleClick = () =>{
        this.setState({favoriteColor:"blue"})
    }
    render(){
        return(
            <header>
                <h1>My Favorite Color is {this.state.favoriteColor}</h1>
                <button onClick={this.handleClick}>Change color to Blue</button>
            </header>
        )
    }
    componentDidMount(){
        setTimeout(() => {
            this.setState({favoriteColor:"yellow"})
        }, 5000);
    }
}

export default ColorC