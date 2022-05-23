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
import ProblemImage from "../parts/ProblemImage";

// ACTIONS
import { getProblems } from "../../store/actions/SkriptaActions";
import { toggleEditingView } from "../../store/actions/pageViewActions";
import { togglePrintPreviewView } from "../../store/actions/pageViewActions";

// LOADER
import { Oval } from  'react-loader-spinner'



export default function Skripta() {
    const { skripta_id, section_id, section_order } = useParams();
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getProblems(skripta_id, section_id))
    }, [dispatch])

    const state =  useSelector( (state) => state )
    const sections = useSelector( (state) => state?.sections )
    const view = useSelector( state => state?.page_view )
    const problem_fields = useSelector(state => state.problem_fields)

    const [displaySuccesAlert, setDisplaySuccesAlert] = useState(false)
    const [displayErrorAlert, setDisplayErrorAlert] = useState(false)
    const [downloadLoading, setDownloadLoading] = useState(false)
    const [displayDownloadModal, setDisplayDownloadModal] = useState(false)
    const [downloadLink, setDownloadLink] = useState('')

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
        if(view.printing) dispatch(togglePrintPreviewView(prevState))
    }

    const handlePrintingToggle = () => {
        let prevState = view.printing ? view.printing : false
        dispatch(togglePrintPreviewView(!prevState))
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
                    setDisplayDownloadModal(true)
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
        setDownloadLoading(!downloadLoading)
        let apiUrl = `${window.location.origin}/api/skripta/print`;
        let printElement = document.querySelector('#printThis')
        
        let formData = new FormData();
        formData.append('html', JSON.stringify(printElement.innerHTML) ) 
        formData.append('id', skripta_id)
        
        axios.post(
            apiUrl,
            formData,
            {
                headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"}
            }
        ).then(res => {
            console.log(`Successfully sent form data`);
            console.log(JSON.parse(res.data).file)
            setDownloadLink(JSON.parse(res.data).file)
            setDisplayDownloadModal(!displayDownloadModal)
        })
        .catch(err => {
            console.log(err);
            setDownloadLoading(!downloadLoading)
            setDisplayDownloadModal(!displayDownloadModal)
        })
        setDownloadLoading(!downloadLoading)
    }

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    {displayErrorAlert && 
                        <div className="alert alert--error">
                            <span>Podatci neuspješno spremljeni u bazu! Zovi 112 (ili Marka)</span>
                            <button onClick={closeAlert}>
                                <FontAwesomeIcon icon={faTimes} />
                            </button>
                        </div>}
                    {displaySuccesAlert &&
                        <div className="alert alert--succes">
                            <span>Podatci uspješno spremljeni u bazu!</span>
                            <button onClick={closeAlert}>
                                <FontAwesomeIcon icon={faTimes} />
                            </button>
                        </div>}
                    <form id="printThis" onSubmit={handleSubmit} className={`skripta-${skripta_id}`}>
                        <div className="only-print frontcover"></div>
                        <div className="problems-section__actions">
                            <button type="button" onClick={handleEditingToggle} className={`problems-section__edit ${view.editing && 'active'}`}>
                                <FontAwesomeIcon icon={faPen} />
                            </button>
                            <button type="button" onClick={handlePrintingToggle} className={`problems-section__print ${view.printing && 'active'}`}>
                                <FontAwesomeIcon icon={faPrint} />
                            </button>
                            <button type="submit" className="btn btn--save">Save</button>
                            <button type="button" onClick={handlePrint} className="btn btn--primary">
                                { downloadLoading ?
                                    <Oval    
                                        heigth="16"
                                        width="16"
                                        color='grey'
                                        ariaLabel='loading'>
                                    </Oval> : 'Print'}
                            </button>
                            {displayDownloadModal &&
                                <div className="problems-section__modal">
                                    <h3>Skripta je spremna za preuzimanje</h3>
                                    <a className="btn btn--primary" href={downloadLink} target="_blank">Preuzmi</a>
                                </div>
                            }
                        </div>
                        <div className="problems-section">
                            {sections.map((section, section_index) => {
                                return(
                                    <a href={`#${section.id}`}>
                                        <h3 className="problems-section__link">{section_order ? section_order : section_index+1}. {section.name}</h3>
                                    </a>
                                )
                            })}
                        </div>
                        <div>
                            {sections.map((section, section_index) => {
                                if (section.problems.length > 0 || section.equations.length > 0 ) {
                                    return (
                                        <div key={section.name} id={section.id}>
                                            <div className="problems-section">
                                                <div className="problems-section__header">
                                                    <h3 className="problems-section__title">{section_order ? section_order : section_index+1}. {section.name}</h3>
                                                </div>
                                                {section.equations.length > 0 &&
                                                    <div className="problems-section__equations">
                                                        <h4 className="problems-section__equations-title">Formule</h4>
                                                        {section.equations.map( equation => {
                                                            return (
                                                                <div key={equation.id} className="problems-section__equation">
                                                                    <div className="problems-section__equation-name">
                                                                        {equation.name}
                                                                    </div>
                                                                    <div className="problems-section__equation-latex">
                                                                        $ {equation.equation} $
                                                                    </div>
                                                                </div>
                                                            )
                                                        })}
                                                    </div>
                                                }
                                                {section.problems.map((problem, index) => {
                                                    return (
                                                        <Problem 
                                                            key={problem.id} 
                                                            sectionIndex={section_order ? section_order : section_index+1}
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
                        {sections.length > 0 &&
                            <div className="problems-section">
                                <div>
                                    {sections.map((section, section_index) => {
                                        if (section.problems.length > 0) {
                                            return (
                                                <div className="solutions-table" key={section.id}>
                                                    <h4 className="solutions-table__title">{section.name}</h4>
                                                    {section.problems.map((problem, index) => {
                                                        return (
                                                            <div className="solutions-table__item" key={problem.id}>
                                                                {problem.question.correct_answer.map(answer => {
                                                                    return (
                                                                        <div key={answer.id}>
                                                                            <span className="solutions-table__number">{section_order ? section_order : section_index+1}.{index+1}.</span>
                                                                            {answer?.answer_choice?.images.length > 0 ? 
                                                                                answer?.answer_choice?.images.map( image => {
                                                                                    return (
                                                                                        <ProblemImage image={image} key={image.id}></ProblemImage>
                                                                                    )
                                                                                }) :
                                                                                answer?.answer_choice?.choice_text
                                                                            }
                                                                            {answer?.answer_text}
                                                                            {answer?.images.length > 0 && answer?.images.map( image => {
                                                                                    return (
                                                                                        <ProblemImage image={image} key={image.id}></ProblemImage>
                                                                                    )
                                                                                })}
                                                                        </div>
                                                                    )
                                                                })}
                                                                { problem.question.subquestions.length > 0 && 
                                                                    <span className="solutions-table__number">{section_order ? section_order : section_index+1}.{index+1}.</span>
                                                                }
                                                                {problem.question.subquestions.map( subquestion => {
                                                                    return(
                                                                        <div>
                                                                            {subquestion.correct_answer.map(answer => {
                                                                                return (
                                                                                    <div key={answer.id}>
                                                                                        {answer?.answer_choice?.choice_text}
                                                                                        {answer?.answer_text}
                                                                                        {answer?.answer_choice?.images.map( image => {
                                                                                            <ProblemImage image={image} key={image.id}></ProblemImage>
                                                                                        })}
                                                                                    </div>
                                                                                )
                                                                            })}
                                                                        </div>
                                                                    )
                                                                })}
                                                            </div>
                                                        )
                                                    })}
                                                </div>
                                            )
                                        }
                                    })}
                                </div>
                            </div>
                        }
                    </form>
                </Layout.Section>
            </Layout>
        </Page>
    )
}