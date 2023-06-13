import React from "react";

class Color extends React.Component {
    constructor(){
        super()
        this.state = {
            favoriteColor : "red",
        }
    }
    handleClick = () =>{
        this.setState({favoriteColor:"blue"})
    }
    shouldComponentUpdate(){
        console.log('after update')
        return true
    }
    getSnapshotBeforeUpdate(){
        console.log("in getSnapshotBeforeUpdate")
    }
    componentDidMount(){
        setTimeout(() => {
            this.setState({favoriteColor:"yellow"})
        }, 5000);
    }
    render(){
        return(
            <header>
                <h1>My Favorite Color is {this.state.favoriteColor}</h1>
                <button onClick={this.handleClick}>Change color to Blue</button>
            </header>
        )
    }
}

class Child extends React.Component {
    constructor(){
        super()
        this.state = {
            show : true,
        }
    }
    componentWillUnmount(){
        alert("component named header will unmount")
    }
    deleteHeader = () => {
        this.setState({show:false})
        this.componentWillUnmount()
    }
    render(){
        const header = this.state.show ? <h1>Hello World</h1> : null;
        return(
            <>
                {header}
                <button onClick={this.deleteHeader}>Delete Header</button>
            </>
        )
    }
}

export {
    Color,
    Child,
}