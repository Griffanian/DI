import React from 'react'

class BuggyCounter extends React.Component {
    constructor(){
        super()
        this.state = {
            count : 0
        }
    }
    handleClick = () => {
        this.setState({count:this.state.count+1})
    }
    render() {
        if (this.state.count >= 5){
         throw Error('something went wrong...')
        }
        return (
            <div onClick={this.handleClick}>
                <h1>{this.state.count}</h1>
            </div>
        );
    }
}
export default BuggyCounter