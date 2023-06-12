import React from "react";

class EventsC extends React.Component {
    constructor(){
        super()
        this.state = {
            value : '',
            isToggleOn : true,
        }
    }
    clickMe = () => {
        alert("I was Clicked")
    }
    handleChange = (event) => {
        this.setState({value: event.target.value});
    }

    handleKeyDown = (event) => {
        if (event.keyCode === 13){
            alert(`The Enter key was pressed, your input is: ${this.state.value}`)
            this.setState({value:''})
        }
    }
    toggleOn = () => {
        this.setState({isToggleOn:!this.state.isToggleOn})
    }
    render(){
        return(
            <>
                <button onClick={this.clickMe}>Click Me</button>
                <input type="text" onKeyDown={this.handleKeyDown} onChange={this.handleChange} placeholder="Press the Enter to submit" value={this.state.value}/>
                <button onClick={this.toggleOn}>{this.state.isToggleOn ? "On":"Off"}</button>
            </>
        )
    }
}

export default EventsC