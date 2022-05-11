// REACT & REDUX
import React, { useState, useEffect } from "react";
import { useParams } from 'react-router';

// SHOPIFY
import {Page, Layout, SkeletonBodyText, Card} from '@shopify/polaris';

// CUSTOM COMPONENTS
import AutocompleteSelect from "../parts/AutocompleteSelect";

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

const CheatsheetPage = () => {
    const { cheatsheet_id } = useParams();
    const apiUrl = `${window.location.origin}/api/cheatsheets/${cheatsheet_id}`
    const { data, loading, error } = useFetch(apiUrl)
    const [layout, setLayout] = useState(null)

    if (loading) return <SkeletonBodyText />; 
    if (error) return "Error!"; 

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    <Card sectioned>
                        <Card.Section key={1}>
                            <AutocompleteSelect label="Pick layout" data={data.layouts} setData={setLayout}></AutocompleteSelect>
                        </Card.Section>
                        <Card.Section key={2}>
                            {data?.name}
                            {data?.cheatsheet_sections.map(section => {
                                return (
                                    <div className="problems-section__equations" key={section.id}>
                                        <h4 className="problems-section__equations-title">{section.name}</h4>
                                        {section.equations.map(equation => {
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
                                )
                            })}
                            
                        </Card.Section>
                        <Card.Section key={3}>
                            {data?.cheatsheet_tables.map(table => {
                                return (
                                    <div key={table.id}>
                                        {table.name}
                                        {table.equations.map(equation => {
                                            return (
                                                <span key={equation.id}>
                                                    ${equation.equation}$
                                                </span>
                                            )
                                        })}
                                    </div>
                                )
                            })}
                        </Card.Section>
                    </Card>
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default CheatsheetPage;