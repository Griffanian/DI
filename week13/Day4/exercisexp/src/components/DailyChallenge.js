import React from "react"

class DailyChallenge extends React.Component{
    constructor(){
        super()
        this.state = {
            data: [],
            postInput:'',
        }
    }
    getHello = async () => {
        try{
            const res = await fetch('http://localhost:3030/api/hello')
            const data = await res.text()
            this.setState({data:data})
        } catch(err){
            console.log(err)
        }
    }
    postToServer = async (e) => {
        e.preventDefault()
        try{
            const res = await fetch('http://localhost:3030/api/world', {
                body: JSON.stringify(s),
                method: 'POST',
                mode: 'no-cors',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                }
            })
            const data = await res
            console.log(data)
        } catch(err){
            console.log(err)
        }
    }
    componentDidMount = () => {
        this.getHello()
    }
    render(){
        if (this.state.data){
            return(
                <div style={{'display':'flex','justifyContent':'center','alignItems':'center','flexDirection':'column'}}>
                    <h1>{this.state.data}</h1>
                    <form onSubmit={this.postToServer}>
                        <input type="text" name="postInput" onChange={(e) => this.setState({postInput:e.target.value})}/>
                        <input  type='submit' value="Send Post"/>
                    </form>

                </div>
            )
        }
    }
}

export default DailyChallenge