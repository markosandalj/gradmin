// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import classNames from "classnames";

// SHOPIFY 

// CUSTOM HOOKS

// CUSTOM COMPONENTS

// STYLES
import './Equation.scss'

import viewType from '../../helpers/viewType';

export default function EditField({ image, text, value, id }) {
    const state =  useSelector( (state) => state )
    const view = useSelector( state => state.view )


    if(!viewType(view).editing) return;

    return (
        <>
            {text && 
                <TextField
                    value={value}
                    onChange={handleChange}
                    readOnly={false}
                    multiline={3}
                    id={id}
                />}
            {image && 
                <DropZone accept="image/*" type="image" allowMultiple={false} onDrop={handleDropZoneDrop}>
                    {fileUpload}
                    {file && file.name}
                </DropZone>}
        </>
    )
}
