import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';

import {AppProvider, Page, Card, Button, Layout} from '@shopify/polaris';
import { Sortable } from '@shopify/draggable';
import { Link } from "react-router-dom";
import useFetch from "../hooks/useFetch";


export default function SkriptaSections() {
    const { skripta_id } = useParams();
    const apiUrl = `http://127.0.0.1:8000/api/skripta/${skripta_id}/list`
    const { data, loading, error } = useFetch(apiUrl)

    if (loading) return "Loading..."; 
    if (error) return "Error!"; 

    return(
        <Page>
        <Layout>
            <Layout.Section>
                {data[0].sections.map( (section, section_index) => {
                    return (
                        <Card sectioned key={section.id}>
                            <Link to={'/index/skripta/'+skripta_id+'/'+section.id}>{section_index+1}. {section.name}</Link>
                        </Card>
                    )
                  })}
              </Layout.Section>
        </Layout>
    </Page>
    )
}