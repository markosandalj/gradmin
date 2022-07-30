export const mathjaxTypeset = () => {
    if( !window.MathJax ) return;
    
    window.MathJax
        .typesetPromise()
        .catch((err) => {
            console.log('Typeset failed: ' + err.message)
        })
}