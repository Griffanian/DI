import React from "react"
import { connect } from "react-redux";
import './App.css';
class App extends React.Component{
  constructor() {
    super()
    this.state = {
      property_one: 'text one'
    }
  }
  render(){
    return (
          <div className="App">
            <header className="App-header">
              <h2>Redux Example</h2>
              <div>{this.state.property_one}</div>
              <div>{this.props.a}</div>
              <div>{this.props.b}</div>
            </header>
          </div>
        );
  }
}

const mapStateToProps = (state) => {
  return {
    a: state.property_one,
    b:state.property_two
  }
}

export default connect(mapStateToProps)(App)



// import {useState} from  'react'
// import Test from './components/Test';


// function App() {
//   const [title,setTitle] = useState('My title')
//   
// }

// export default App;
