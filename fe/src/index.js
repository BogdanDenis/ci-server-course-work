import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createBrowserHistory } from 'history';
import { Router } from 'react-router';
import { routerMiddleware } from 'react-router-redux';
import { apiMiddleware } from 'redux-api-middleware';
import thunk from 'redux-thunk';
import {
  createStore,
  applyMiddleware,
} from 'redux';

import './index.scss';

import App from './app';
import { rootReducer } from './reducers/index';

const history = createBrowserHistory();
const middleware = routerMiddleware(history);
const createStoreWithMiddleware = applyMiddleware(
  middleware,
  apiMiddleware,
  thunk,
)(createStore);

const store = createStoreWithMiddleware(
  rootReducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
);

window.store = store;

ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      <App />
    </Router>
  </Provider>
  , document.getElementById('root'),
);
