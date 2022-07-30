import React from 'react'

// COMPONENTS
import { EditableTextField } from './EditableTextField'

// STYLES
import styled from 'styled-components';

// UTILS
import { formatLatex } from '../utils/formatLatex';


const EquationName = styled.div`
    font-weight: bold;
    font-size: .875rem;
    text-transform: uppercase;
`

const StyledEquation = styled.div`
    padding-left: .75rem;
    position: relative;
`

export const Equation = ({ equation }) => {

    if(!equation) return <></>;

    return (
        <>
            <EditableTextField 
                value={equation.name}
                id={equation.id}
            />
            <EditableTextField 
                value={formatLatex(equation.equation)}
                id={equation.id}
                containsMath
            />
        </>
    )
}
