import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reducer from './redux/reducers/index'
import {createStore,applyMiddleware} from 'redux'
import { Provider } from 'react-redux';
// import thunk from 'redux-thunk'
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
// const middlewareEnhancer = applyMiddleware(thunk,first)
const store = createStore(reducer)

root.render(
  <React.StrictMode>
    <Provider store={store} >
      <App/>
    </Provider>
  </React.StrictMode>
);