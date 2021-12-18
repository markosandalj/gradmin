import './index.scss'
// import '@shopify/polaris/dist/styles.css';
// import { Sortable } from '@shopify/draggable';
// import store from './store/store';
// import App from './components/App';
import './components/alpine';

function initializeMathJax() {
    if (document.body.querySelector('#app') ||
    document.body.textContent.match(/(?:\$|\\\(|\\\[|\\begin\{.*?})/)) {
            if (!window.MathJax) {
                window.MathJax = {
                    tex: {
                        inlineMath: {'[+]': [['$', '$']]}
                    },
                    svg: {fontCache: 'global'}
                };
            }
            var script = document.createElement('script');
            script.setAttribute('id', 'MathJaxScriptTag')
            script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
            // script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
            document.head.appendChild(script);
    }
}

setTimeout( () => {
    initializeMathJax()
    // const sortable = new Sortable(document.querySelectorAll('.problems-section'), {
    //     draggable: '.drag-item',
    //     handle: '.drag-handle'
    // })
}, 200)