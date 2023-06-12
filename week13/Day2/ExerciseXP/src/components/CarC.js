import React from "react";
import Garage from "./Garage";

class CarC extends React.Component {
    constructor(){
        super()
        this.state = {
            color : "Black"
        }
    }
    render(){
        return(
            <header>
                <p>Name: {this.props.carinfo.name}</p>
                <p>Model: {this.props.carinfo.model}</p>
                <p>Color: {this.state.color}</p>
                <Garage size="small"/>
            </header>
        )
    }
}

export default CarC