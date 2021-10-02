import React, { Component, useState, useEffect } from 'react';
import { useParams } from 'react-router';

import { Page, Card, Layout } from '@shopify/polaris';
import { Sortable } from '@shopify/draggable';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPen, faPrint } from '@fortawesome/free-solid-svg-icons';

import Problem from '../parts/Problem';
import useFetch from '../hooks/useFetch';

export default function SkriptaPrint() {
    const { subject, id } = useParams();
    const apiUrl = `http://127.0.0.1:8000/api/skripta/${subject}`
    const { data, loading, error } = useFetch(apiUrl)

    const mathTypeset = () => {
        if( window.MathJax ) {
            console.log('MathJax typset succesfull')
            window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
        }
    }

    useEffect(() => {
        mathTypeset()
    }, [])

    if (loading) return 'Loading...';
    if (error) return 'Error!';

    const handlePrint = () => {
        if(!isPrintingActive) handlePrintingToggle();
        setTimeout( () => {
            window.print()
        }, 100)
    }

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    <div id='printThis'>
                    {data.map((section) => {
                        if (section.problems.length > 0) {
                            return (
                                <Card sectioned key={section.id}>
                                    <div>
                                        <div className='problems-section__header'>
                                            <h3 href='https://gradivo.hr' className='problems-section__title'>{section.order}. {section.name}</h3>
                                            <div className='problems-section__actions'>
                                                <button type='button' onClick={handleEditingToggle} className={`problems-section__edit ${isEditingActive ? 'active' : null}`}>
                                                    <FontAwesomeIcon icon={faPen} />
                                                </button>
                                                <button type='button' onClick={handlePrintingToggle} className={`problems-section__print ${isPrintingActive ? 'active' : null}`}>
                                                    <FontAwesomeIcon icon={faPrint} />
                                                </button>
                                                <button type='submit' className='btn btn--save'>Save</button>
                                                <button type='button' onClick={handlePrint} className='btn btn--primary'>Print</button>
                                            </div>
                                        </div>
                                        {section.problems.map((problem, index) => {
                                            return (
                                                <Problem 
                                                    key={problem.id} 
                                                    problem={problem} 
                                                    isEditingActive={isEditingActive} 
                                                    isPrintingActive={isPrintingActive} 
                                                    problem_index={index} 
                                                    section_index={section.order}
                                                ></Problem>
                                            )
                                        })}
                                    </div>
                                </Card>
                            )
                        } 
                        // else {
                        //     return (
                        //         <h3>Za ovo gradivo ne postoje zadatci</h3>
                        //     )
                        // }
                    })}
                    </div>
                </Layout.Section>
            </Layout>
        </Page>
    )
}