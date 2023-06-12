import React from 'react';

class VotingC extends React.Component{
    constructor(){
        super()
        this.state = {
            languages : [
                {name: "Php", votes: 0},
                {name: "Python", votes: 0},
                {name: "JavaSript", votes: 0},
                {name: "Java", votes: 0}
            ]
        }
    }
    changeVote = (e,index) => {
        e.preventDefault()
        const newArray = this.state.languages.map((obj) => {
            if ( this.state.languages.indexOf(obj) === index) {
              return { ...obj, votes:this.state.languages[index].votes+1 };
            }
            return obj;
          });
          this.setState({languages : newArray});
        }
    render(){
        return(
            <>
                <h1>Vote Your languages</h1>
                {this.state.languages.map((element, index) => {
                        return(<div key={index} style={{
                            display : "flex",
                            backgroundColor : "peachpuff",
                            justifyContent : 'space-around',
                            alignContent : "center",
                            width : "300px",
                        }}>
                            <p>{element.votes}</p>
                            <h5>{element.name}</h5>
                            <a onClick={(e) => this.changeVote(e,index)} style={{height:"fit-content", margin: "auto 0"}} href='/'>Click Here</a>
                        </div>)
                    })
                }
            </>
        )
    }
}

export default VotingC