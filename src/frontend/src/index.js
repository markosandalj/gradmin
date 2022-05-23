import './index.scss'
import '@shopify/polaris/dist/styles.css';
// import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import { Sortable } from '@shopify/draggable';
import store from './es6/store/store';
import App from './es6/components/App';

function initializeMathJax() {
    if (document.body.querySelector('#app') ||
    document.body.textContent.match(/(?:\$|\\\(|\\\[|\\begin\{.*?})/)) {
            if (!window.MathJax) {
                window.MathJax = {
                    tex: {
                        inlineMath: {'[+]': [['$', '$']]}
                    },
                    svg: {fontCache: 'local'}
                };
            }
            var script = document.createElement('script');
            script.setAttribute('id', 'MathJaxScriptTag')
            script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
            // script.src = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full'
            // script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
            document.body.appendChild(script);
    }
}

setTimeout( () => {
    initializeMathJax()
    const sortable = new Sortable(document.querySelectorAll('.problems-section'), {
        draggable: '.drag-item',
        handle: '.drag-handle'
    })
}, 1500)