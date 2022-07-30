import React from "react";
import { createRoot } from "react-dom/client";
import { store } from './store/store'
import { Provider } from 'react-redux';

// STYLES
import './index.scss'

// SHOPIFY 
import '@shopify/polaris/build/esm/styles.css';

import { App } from './App';
import { initializeMathJax } from "./utils/mathjaxInit";
// import './index.scss'

const container = document.getElementById("app");
if(container) {
    const root = createRoot(container);
    root.render(
        <Provider store={store}>
            <App />
        </Provider>
    );
}

setTimeout( () => {
    initializeMathJax()
}, 1500)