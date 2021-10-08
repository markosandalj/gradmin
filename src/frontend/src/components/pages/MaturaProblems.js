
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
import { faList, faPen, faSearchPlus, faTools, faTimes } from '@fortawesome/free-solid-svg-icons'

// ACTIONS
import { toggleEditingView, toggleSitePreviewView } from "../../store/actions/problemsViewActions";

const MaturaProblems = () => {
    const { matura_id } = useParams();
    const apiUrl = `${window.location.origin}/api/matura/${matura_id}`
    const { data, loading, error } = useFetch(apiUrl)

    const dispatch = useDispatch()
    const view = useSelector( state => state?.problems_view )
    const problem_fields = useSelector(state => state.problem_fields)

    const [displaySuccesAlert, setDisplaySuccesAlert] = useState(false)
    const [displayErrorAlert, setDisplayErrorAlert] = useState(false)

    const closeAlert = () => {
        setDisplaySuccesAlert(false);
        setDisplayErrorAlert(false);
    }

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

    const handleSubmit = (event) => {
        event.preventDefault();

        if(Object.keys(problem_fields).length > 0) {
            let formData = new FormData();
            
            for(const [key, value] of Object.entries(problem_fields)){
                formData.append(key, JSON.stringify(value) )
            };
            console.log(...formData)
            let apiUrl = window.location.origin + '/api/question/update';
            axios.post(
                    apiUrl,
                    formData,
                    {
                        headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"}
                    }
                ).then(res => {
                    setDisplaySuccesAlert(true);
                    console.log(`Successfully sent form data` + res.data);
                })
                .catch(err => {
                    console.log(err);
                    setDisplayErrorAlert(true)
                })
        } else {
            console.log(problem_fields)
            console.log(state)
            console.log('Empty')
        }
    }
    
    const matura = data[0];
    let matura_name = matura.subject.level != 0 ? matura.subject.subject_name + ' ' + matura.subject.level : matura.subject.subject_name;
    
    return (
        <Page>
            <Layout>
                <Layout.Section>
                    {displayErrorAlert && 
                        <div className="alert alert--error">
                            <span>Podatci uspješno spremljeni u bazu!</span>
                            <button onClick={closeAlert}>
                                <FontAwesomeIcon icon={faTimes} />
                            </button>
                        </div>}
                    {displaySuccesAlert &&
                        <div className="alert alert--succes">
                        <span>Podatci neuspješno spremljeni u bazu! Zovi 112 (ili Marka)</span>
                            <button onClick={closeAlert}>
                                <FontAwesomeIcon icon={faTimes} />
                            </button>
                        </div>}
                    {/* <form onSubmit={handleSubmit}> */}
                        <div className="matura__header">
                            <h3 className="problems-section__title">{`${matura_name} - ${matura.year.year}. ${matura.term.term}`}</h3>
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
                                <button onClick={handleSubmit} className="btn btn--save">Save</button>
                            </div>
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
                    {/* </form> */}
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default MaturaProblems;