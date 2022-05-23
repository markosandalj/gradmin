export const typsetMathjax = () => {
    if( window.MathJax ) {
        console.log("MathJax typset succesfull")
        return window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
    }
}