import Products from './components/Products';
import Product from './components/Product';
import { Routes,Route } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Routes>
          <Route path='/product' element={<Products/>}></Route>
          <Route path='/product/:id' element={<Product/>}></Route>
        </Routes>
      </header>
    </div>
  );
}

export default App;
