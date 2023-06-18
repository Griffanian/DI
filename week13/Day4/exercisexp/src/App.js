// import ErrorBoundary from './components/ErrorBoundary';
// import Home from './components/Home';
// import Profile from './components/Profile';
// import Shop from './components/Shop';
// import { BrowserRouter, Routes, Route, NavLink, Router, RouterProvider } from "react-router-dom";
// import PostList from "./components/PostList";
// import { Example1,Example2,Example3 } from "./components/Exercise3";
import DailyChallenge from './components/DailyChallenge';
import { useState} from 'react';
import { Button } from "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const sendData = async () => {
    const obj = JSON.stringify({
      key1: 'myusername',
      email: 'mymail@gmail.com',
      name: 'Isaac',
      lastname: 'Doe',
      age: 27
    });

    try {
     fetch("https://webhook.site/31a7cfb7-0cb7-4f5c-90de-444eaefa5cf4", {
        body: obj,
        method: 'POST',
        mode: 'no-cors',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      }).then(res => res)
      .then(data => console.log(data))
    } catch (error) {
      console.error('error: ' + error);
    }
  }
  return (
  // Exercise 1

  //  <BrowserRouter>
  //     <nav class="nav nav-pills">
  //       <NavLink className={"nav-link"} to={"/"}>Home</NavLink>
  //       <NavLink className={"nav-link"} to={"/profile"}>Profile</NavLink>
  //       <NavLink className={"nav-link"} to={"/shop"}>Shop</NavLink>
  //     </nav> 

  //     <Routes>
  //       <Route  path="/" element={<ErrorBoundary><Home /></ErrorBoundary>} />
  //       <Route path="/profile" element={<ErrorBoundary><Profile /></ErrorBoundary>} />
  //       <Route path="/shop" element={<ErrorBoundary><Shop /></ErrorBoundary>} />
  //     </Routes>
  //   </BrowserRouter>

    // Exercise 2

    // <PostList />

    // Exercise 3 

    // <Example1 />
    // <Example2 />
    // <Example3 />

    // Exercise 4 
    
    // <>
    //   <button onClick={sendData}>Send Data</button>
    //   <p>{JSON.stringify(data)}</p>
    // </>

    // Daily Challenge
    <DailyChallenge />
  );
}

export default App;
