
// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from 'axios'

// SHOPIFY
import {Page, Layout} from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

// COMPONENTS
import Problem from "../parts/Problem";

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faList, faPen, faSearchPlus, faTools } from '@fortawesome/free-solid-svg-icons'

// ACTIONS
import { toggleEditingView, toggleSitePreviewView } from "../../store/actions/problemsViewActions";

const MaturaProblems = () => {
    const { matura_id } = useParams();
    const apiUrl = `${window.location.origin}/api/matura/${matura_id}`
    const { data, loading, error } = useFetch(apiUrl)

    const dispatch = useDispatch()
    const view = useSelector( state => state?.problems_view )

    if (loading) return "Loading..."; 
    if (error) return "Error!"; 

    const mathTypeset = () => {
        if( window.MathJax ) {
            console.log("MathJax typset succesfull")
            window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
        }
    }

    const handleEditingToggle = () => {
        let prevState = view.editing ? view.editing : false
        dispatch(toggleEditingView(!prevState))
        if(view.site_preview) dispatch(toggleSitePreviewView(prevState))
    }

    const handleSitePreviewToggle = () => {
        let prevState = view.site_preview ? view.site_preview : false
        dispatch(toggleSitePreviewView(!prevState))
        if(view.editing) dispatch(toggleEditingView(prevState))
    }
    
    return (
        <Page>
            <Layout>
                <Layout.Section>
                    <div className="matura__actions">
                    <button type="button" onClick={mathTypeset} className={`problems-section__edit`}>
                            <FontAwesomeIcon icon={faTools} />
                        </button>
                        <button type="button" onClick={handleEditingToggle} className={`problems-section__edit ${view.editing && 'active'}`}>
                            <FontAwesomeIcon icon={faPen} />
                        </button>
                        <button type="button" onClick={handleSitePreviewToggle} className={`problems-section__preview ${view.site_preview && 'active'}`}>
                            <FontAwesomeIcon icon={faSearchPlus} />
                        </button>
                        <button className="btn btn--save">Save</button>
                    </div>
                    {data[0].problems.map( (problem, index) => {
                        return (
                            <div className='problems-section' key={problem.id}>
                                <Problem 
                                    key={problem.id}
                                    problem_index={index} 
                                    problem={problem}
                                ></Problem>
                            </div>
                        )
                    })} 
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default MaturaProblems;