import React, { Component, useState, useEffect } from "react";
import axios from 'axios'
import { useParams } from 'react-router';

import {AppProvider, Page, Card, Layout} from '@shopify/polaris';
import Problem from "../parts/Problem";


const ProblemsByMaturaList = () => {
  const { id, subject } = useParams();
  const apiUrl = id ? `http://127.0.0.1:8000/api/maturas/${subject}/${id}` : `http://127.0.0.1:8000/api/maturas/${subject}`
  const { data, loading, error } = useFetch(apiUrl)

  if (loading) return "Loading..."; 
  if (error) return "Error!"; 

  return (
    <Page>
      <Layout>
        <Layout.AnnotatedSection
          title="Account details"
          description="Jaded Pixel will use this as your account information."
        >
          <Card title="Matura zadatci" sectioned>
            {data.map( matura => {
              return (
                matura.problems.map( problem => {
                  return (
                    <Problem key={problem.name} problem={problem}></Problem>
                  )
                })
                )
              })}
          </Card>
        </Layout.AnnotatedSection>
      </Layout>
    </Page>
  );
}


export default ProblemsByMaturaList;
