import React, { useState } from 'react'

// COMPONENTS
import { Equation } from './Equation'

// STYLES
import styled from 'styled-components'

const Table = styled.div`
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 2rem;
    padding: 1.5rem;
    border-radius: .75rem;
    border: 2.5px solid rgba(0, 0, 0, 0.2);
    margin: 1.5rem 0;
    position: relative;
`

const TableTitle = styled.div`
    position: absolute;
    bottom: 100%;
    background: var(--white);
    z-index: 1;
    padding: .5rem .75rem;
    left: .75rem;
    transform: translateY(46%);
    text-transform: uppercase;
    font-size: .75rem;
    font-weight: bold;
    color: rgba(0, 0, 0, .5);
`

const TableItem = styled.div`
    display: flex;
    flex-direction: column;
    gap: .5rem;
    margin-bottom: 1rem;
    margin-right: 2rem;
`

export const EquationsTable = ({ equations, tableTitle }) => {
    const [title, setTitle] = useState(tableTitle || 'Formule')

    if(!equations) return <></>;

    return (
        <Table>
            <TableTitle>{title}</TableTitle>
            {equations.map(equation => {
                return (
                    <TableItem>
                        <Equation equation={equation} />
                    </TableItem>
                )
            })}
        </Table>
    )
}
