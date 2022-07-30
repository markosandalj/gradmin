// STYLES
import styled from 'styled-components'

export const FixedFullscreenBar = styled.div`
    position: fixed;
    top: 3.5rem;
    left: calc(15rem + env(safe-area-inset-left));
    width: 100%;
    max-width:  calc(100vw - 15rem - env(safe-area-inset-left));
    background-color: white;
    padding: 0.75rem  var(--p-space-6);
    z-index: 200;

    @media screen and (max-width: 769.99px) {
        left: 0;
        max-width: 100vw;
    }
`