import styled from "styled-components"

export const FloatingEditButton = styled.button`
    color: ${props => props.active ? 'var(--primary)' : 'var(--black)'}
`