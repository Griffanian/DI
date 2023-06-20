import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Counter from './components/Counter';
import Age from './components/Age';
import reducer from './reducers/index';
import {createStore,applyMiddleware} from 'redux'
import { first } from './middles';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk'
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
const middlewareEnhancer = applyMiddleware(thunk,first)
const store = createStore(reducer,middlewareEnhancer)

root.render(
  <React.StrictMode>
    <Provider store={store} >
      <Age />
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
