
// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { Link } from "react-router-dom";
import axios from 'axios'

// SHOPIFY
import {Page, Layout} from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

// COMPONENTS
import Problem from "../parts/Problem";

const MaturaProblems = () => {
    const { matura_id } = useParams();
    const apiUrl = `${window.location.origin}/api/matura/${matura_id}`

    const { data, loading, error } = useFetch(apiUrl)

    if (loading) return "Loading..."; 
    if (error) return "Error!"; 

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    <div className='problems-section'>
                        {data[0].problems.map( (problem, index) => {
                            return (
                                <Problem 
                                    key={problem.id}
                                    problem_index={index} 
                                    problem={problem}
                                ></Problem>
                                )
                            })} 
                    </div>
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default MaturaProblems;