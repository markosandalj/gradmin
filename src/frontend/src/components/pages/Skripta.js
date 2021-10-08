// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

// SHOPIFY
import { Page, Layout } from '@shopify/polaris';
import { Sortable } from '@shopify/draggable';

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPen, faPrint, faPlus, faTimes } from '@fortawesome/free-solid-svg-icons';

// COMPONENTS
import Problem from "../parts/Problem";

// ACTIONS
import { getProblems } from "../../store/actions/SkriptaActions";
import { toggleEditingView } from "../../store/actions/problemsViewActions";
import { togglePrintingView } from "../../store/actions/problemsViewActions";



export default function Skripta() {
    const { skripta_id, section_id, section_order } = useParams();
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getProblems(skripta_id, section_id))
    }, [dispatch])

    const state =  useSelector( (state) => state )
    const sections = useSelector( (state) => state?.sections )
    const view = useSelector( state => state?.problems_view )
    const problem_fields = useSelector(state => state.problem_fields)

    const [displaySuccesAlert, setDisplaySuccesAlert] = useState(false)
    const [displayErrorAlert, setDisplayErrorAlert] = useState(false)

    const closeAlert = () => {
        setDisplaySuccesAlert(false);
        setDisplayErrorAlert(false);
    }

    const mathTypeset = () => {
        if( window.MathJax ) {
            console.log("MathJax typset succesfull")
            window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
        }
    }

    const handleEditingToggle = () => {
        let prevState = view.editing ? view.editing : false
        dispatch(toggleEditingView(!prevState))
        if(view.printing) dispatch(togglePrintingView(prevState))
    }

    const handlePrintingToggle = () => {
        let prevState = view.printing ? view.printing : false
        dispatch(togglePrintingView(!prevState))
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

    useEffect(() => {
        mathTypeset()
    }, [view])

    const sortable = new Sortable(document.querySelectorAll('Polaris-Card > .Polaris-Card__Section'), {
        draggable: '.drag-item',
        handle: '.drag-handle'
    })

    const handlePrint = () => {
        if(!view.printing) handlePrintingToggle();
        setTimeout( () => {
            window.print()
        }, 100)
    }

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
                    <form onSubmit={handleSubmit}>
                        <div className="problems-section__actions">
                            <button type="button" onClick={handleEditingToggle} className={`problems-section__edit ${view.editing && 'active'}`}>
                                <FontAwesomeIcon icon={faPen} />
                            </button>
                            <button type="button" onClick={handlePrintingToggle} className={`problems-section__print ${view.printing && 'active'}`}>
                                <FontAwesomeIcon icon={faPrint} />
                            </button>
                            <button type="submit" className="btn btn--save">Save</button>
                            <button type="button" onClick={handlePrint} className="btn btn--primary">Print</button>
                        </div>
                        <div id="printThis">
                        {sections.map((section) => {
                            if (section.problems.length > 0) {
                                return (
                                    <div key={section.name}>
                                        <div className="problems-section">
                                            <div className="problems-section__header">
                                                <h3 className="problems-section__title">{section_order}. {section.name}</h3>
                                            </div>
                                            {section.problems.map((problem, index) => {
                                                return (
                                                    <Problem 
                                                        key={problem.id} 
                                                        sectionIndex={section.order}
                                                        problem_index={index} 
                                                        problem={problem}
                                                    ></Problem>
                                                )
                                            })}
                                        </div>
                                        <div className="problems-section problems-section__add-new">    
                                            <FontAwesomeIcon icon={faPlus} />
                                        </div>
                                    </div>
                                )
                            }
                        })}
                        </div>
                    </form>
                </Layout.Section>
            </Layout>
        </Page>
    )
}

// import useFetch from "../hooks/useFetch";
// const { data, loading, error } = useFetch(apiUrl)
// if (loading) return "Loading...";
// if (error) return "Error!";