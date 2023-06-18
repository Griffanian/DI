// import Products from './components/Products';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';

import './App.css';
import { Routes,Route,Link } from 'react-router-dom';

function App() {
  return (
    <>
      <nav>
        <Link to='/'><h1>Home</h1></Link>
        <Link to='/about'><h1>About</h1></Link>
        <Link to='/contact'><h1>Contact</h1></Link>
      </nav>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/about' element={<About/>} />
        <Route path='/contact/:id' element={<Contact/>} />
      </Routes>
    </>
  );
}

export default App;
