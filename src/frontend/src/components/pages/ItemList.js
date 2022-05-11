// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { Link } from "react-router-dom";
import axios from 'axios'

// SHOPIFY
import {Page, Layout, SkeletonBodyText } from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

const ItemList = ({ apiUrl, linksPath }) => {
    const { data, loading, error } = useFetch(apiUrl)

    if (loading) return <SkeletonBodyText />;
    if (error) return "Error!"; 

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    {data.map( (item, index) => {
                        return (
                            <div className='problems-section' key={item.id}>
                                <Link to={`linksPath/${id}`} >{item.name}</Link>
                            </div>
                        )
                    })} 
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default ItemList;