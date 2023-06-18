import React from 'react';

class PostList extends React.Component{
    constructor(){
        super()
        this.state = {
            data: []
        }
    }
    getData = () => {
        fetch("./post.json")
        .then(res => res.json())
        .then(data => this.setState({data:data}))
    }
    componentDidMount = () => {
        this.getData()
    }
    render(){
        return(
            <div style={{'display':'flex','flexDirection':'column','justifyContent':'center'}}>
                <h1>Hi This is a Title</h1>
                {
                this.state.data.map(item =>
                        <div key={item.id}>
                            <h2>{item.title}</h2>
                            <p>{item.content}</p>
                        </div>
                    )
                }
            </div>
        )
    }
}  

export default PostList