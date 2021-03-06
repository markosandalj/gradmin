// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { Link } from "react-router-dom";
import axios from 'axios'

// SHOPIFY 
import {Page, Layout, SkeletonBodyText } from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

const MaturaList = () => {
    const { subject_id } = useParams();
    const apiUrl = `${window.location.origin}/api/matura/${subject_id}/list`
    const { data, loading, error } = useFetch(apiUrl)

    if (loading) return <SkeletonBodyText />; 
    if (error) return "Error!"; 

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    {data.map( (matura, matura_index) => {
                        let matura_name = matura.subject.level != 0 ? matura.subject.subject_name + ' ' + matura.subject.level : matura.subject.subject_name;
                        return (
                            <div className='problems-section' key={matura.id}>
                                <Link to={'/index/matura/'+matura.id}>{matura_name} - {matura.year.year}. {matura.term.term}</Link>
                            </div>
                        )
                    })} 
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default MaturaList;