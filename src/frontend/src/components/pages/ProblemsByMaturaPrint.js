import React, { Component, useState, useEffect } from "react";
import axios from 'axios'
import { useParams } from 'react-router';

import { Page, Card, Layout } from '@shopify/polaris';
import ProblemSinglePrint from "../parts/ProblemSinglePrint";
import useFetch from "../hooks/useFetch";


export default function ProblemsByMaturaPrint() {
  const { id, subject } = useParams();
  const apiUrl = id ? `http://127.0.0.1:8000/api/maturas/${subject}/${id}` : `http://127.0.0.1:8000/api/maturas/${subject}`
  const { data, loading, error } = useFetch(apiUrl)

  if (loading) return "Loading..."; 
  if (error) return "Error!"; 
  
  return (
    <Page>
        <Layout>
          <Card>
              <div id="printThis">
                  {data.map( matura => {
                      return (
                          matura.problems.map( problem => {
                              return (
                                  <ProblemSinglePrint key={problem.name} problem={problem}></ProblemSinglePrint>
                              )
                          })
                      )
                  })}
              </div>
          </Card>
        </Layout>
    </Page>
  );
}

