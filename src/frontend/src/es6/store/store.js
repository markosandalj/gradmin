import React from 'react';
import { render } from "react-dom";
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';

import App from '../components/App'

import rootReducer from './reducers/reducers';

const initialState = {
    loading: false,
    error: false,
    problems: [],
};

const middleware = [thunk];

const store = createStore(
    rootReducer,
    compose(applyMiddleware(...middleware))
);

export default  store;

const container = document.getElementById("app");
render(
    <Provider store={store}>
        <App />
    </Provider>
    , container
);