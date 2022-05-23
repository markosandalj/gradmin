// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import classNames from "classnames";

// SHOPIFY 

// CUSTOM HOOKS

// CUSTOM COMPONENTS
import Equation from "../Equation/Equation";

// STYLES
import './EquationSection.scss'


export default function EquationSection({ equations, showEquationNames, name, rounded, colored }) {
    
    const classes = classNames("equation-section", {
        "equation-section--rounded": rounded,
        "equation-section--colored": colored,
    })

	return (
        <div className={classes}>
            <h4 className="equation-section__title">{name}</h4>
            {equations.map(equation => <Equation key={equation.id} id={equation.id} equation={equation.equation} showEquationNames={showEquationNames} name={equation.name} /> )}
        </div>
	);
}
