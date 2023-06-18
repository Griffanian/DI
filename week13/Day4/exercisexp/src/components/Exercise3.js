import React from 'react';

class Example1 extends React.Component{
    constructor(){
        super()
        this.state = {
            data: []
        }
    }
    getData = () => {
        fetch("./data.json")
        .then(res => res.json())
        .then(data => this.setState({data:data}))
    }
    componentDidMount = () => {
        this.getData()
    }
    render(){
        if (this.state.data.length === 0) {
            return (<h1>not yet data</h1>)
        } else {
            return(
                <div style={{'display':'flex','flexDirection':'column','justifyContent':'center'}}>                    
                    <ul>
                        {
                        this.state.data.SocialMedias.map(item =><li key={item}>{item}</li>)
                        }
                    </ul>
                </div>
            )
        }
        
    }
}  

class Example2 extends React.Component{
    constructor(){
        super()
        this.state = {
            data: []
        }
    }
    getData = () => {
        fetch("./data.json")
        .then(res => res.json())
        .then(data => this.setState({data:data}))
    }
    componentDidMount = () => {
        this.getData()
    }
    render(){
        if (this.state.data.length === 0) {
            return (<h1>not yet data</h1>)
        } else {
            return(
                <div style={{'display':'flex','flexDirection':'column','justifyContent':'center'}}>                    
                    {
                    this.state.data.Skills.map(item =>
                        <div>
                            <h5>{item.Area}</h5>
                            <ul>
                            {
                            item.SkillSet.map(lang =><li key={lang.Name}>{lang.Name}</li>)
                            }
                            </ul>   
                        </div>                 
                    )}
                </div>
            )
        }
        
    }
}  

class Example3 extends React.Component{
    constructor(){
        super()
        this.state = {
            data: []
        }
    }
    getData = () => {
        fetch("./data.json")
        .then(res => res.json())
        .then(data => this.setState({data:data}))
    }
    componentDidMount = () => {
        this.getData()
    }
    render(){
        if (this.state.data.length === 0) {
            return (<h1>not yet data</h1>)
        } else {
            return(
                <div style={{'display':'flex','flexDirection':'column','justifyContent':'center'}}>                    
                    {
                    this.state.data.Experiences.map(item =>
                    <div style={{'display':'flex','flexDirection':'column','justifyContent':'center','width':'fit-content'}}>                    
                        <img src={item.logo}></img>
                            <a href={item.url}>{item.companyName}</a>
                            <ul>
                            {
                            item.roles.map(role =>
                                <>
                                    <h5 key={role.title}>{role.title}</h5>
                                    <p key={role.startDate}>{role.startDate} {role.location}</p>
                                    <p key={role.description}>{role.description}</p>
                                </>
                                )
                            }
                            </ul>   
                    </div>                 
                    )}
                </div>
            )
        }
        
    }
}  

export {
    Example1,
    Example2,
    Example3
}
