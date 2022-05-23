// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import classNames from "classnames";

// SHOPIFY 
import { TextField } from '@shopify/polaris'; 

// CUSTOM HOOKS

// CUSTOM COMPONENTS

// STYLES
import './Equation.scss'

// ACTIOSN
import { updateEquation } from "../../../store/actions/CheatsheetActions";

// HELPERS
import viewType from '../../helpers/viewType';

export default function Equation({ id, equation, showEquationNames, name }) {
    const [equationLatex, setEquationLatex] = useState(equation)
    const [equationName, setEquationName] = useState(name)
   
    const dispatch = useDispatch()
    const state =  useSelector( (state) => state )
    const view = useSelector( state => state.view )
    
    const classes = classNames("equation", {})

    const handleChange = (newValue, id) => {
        dispatch(updateEquation(id, newValue))
    }

    return (
        <div className={classes}>
            {showEquationNames && <div className="equation__name">
                {equationName}
            </div>}
            <div className="equation__latex">
                $ {equationLatex} $
                {viewType(view).editing && 
                    <TextField
                        value={equationLatex}
                        onChange={handleChange}
                        readOnly={false}
                        multiline={2}
                        id={id}
                    />}
            </div>
        </div>
    )
}
