// REACT & REDUX
import React, { useState, useEffect } from "react";
import { useParams } from 'react-router';
import { useSelector, useDispatch } from "react-redux";

// SHOPIFY
import {Page, Layout, SkeletonBodyText, Card, Stack, ButtonGroup, Button, Heading } from '@shopify/polaris'; 

// CUSTOM COMPONENTS
import AutocompleteSelect from "../parts/AutocompleteSelect";
import PageActions from "../parts/PageActions";
import EquationSection from "../parts/EquationSection/EquationSection";

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";
import ApiRoutes from "../config/ApiRoutes";

// ACTIONS
import { getCheatsheetData } from "../../store/actions/CheatsheetActions";

const CheatsheetPage = () => {
    const { cheatsheet_id } = useParams();
    const dispatch = useDispatch()
    const state =  useSelector( (state) => state )
    const data = useSelector( (state) => state?.cheatsheet )
    // const apiUrl = ApiRoutes.cheatsheets + cheatsheet_id
    // const { data, loading, error } = useFetch(apiUrl) 
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(false)
    const [layout, setLayout] = useState(data?.layout)

    useEffect(() => {
        setLoading(true)
        dispatch(getCheatsheetData(cheatsheet_id))
        setLoading(false)
    }, [dispatch])


    if (loading) return <SkeletonBodyText />; 
    if (error) return "Error!"; 

    return (
        <Page>
            <Layout>
                <PageActions title={data.name}/>
                <Layout.Section>
                    <Card sectioned key="1213124124">
                        <AutocompleteSelect label="Pick layout" data={data.layouts} setData={setLayout}></AutocompleteSelect>
                    </Card>
                    <Card sectioned key="2123214124" >
                        <div id="printThis">
                            {data?.cheatsheet_sections?.map(section => <EquationSection key={section.id} colored equations={section.equations} name={section.name} /> )}
                            {data?.cheatsheet_tables?.map(table => <EquationSection key={table.id} colored equations={table.equations} name={table.name} /> )}
                        </div>
                    </Card>
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default CheatsheetPage;