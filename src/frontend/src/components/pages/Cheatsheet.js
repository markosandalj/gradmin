// REACT & REDUX
import React, { useState, useEffect } from "react";
import { useParams } from 'react-router';

// SHOPIFY
import {Page, Layout, SkeletonBodyText, Card} from '@shopify/polaris';

// COMPONENTS
import AutocompleteSelect from "../parts/AutocompleteSelect";
import { EquationsTable } from '../EquationsTable';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";
import { cheatsheetFullApiRoute } from "../../settings/apiRoutes";

export const Cheatsheet = () => {
    const { cheatsheet_id } = useParams();
    const { data, loading, error } = useFetch(cheatsheetFullApiRoute(cheatsheet_id))
    const [layout, setLayout] = useState(null)

    if (loading) return <SkeletonBodyText />; 
    if (error) return "Error!"; 

    return (
        <Layout.Section>
            <Card>
                <Card.Section key={1}>
                    <AutocompleteSelect 
                        label="Pick layout" 
                        data={data.layouts} 
                        setData={setLayout}
                    />
                </Card.Section>
            </Card>
            <Card>
                <Card.Section>
                    {data?.name}
                    {data?.cheatsheet_sections.map(section => {
                        return (
                            <EquationsTable 
                                equations={section.equations} 
                                tableTitle={section.name}
                            />
                        )
                    })}
                </Card.Section>
                <Card.Section>
                    {data?.cheatsheet_tables.map(table => {
                        return (
                            <EquationsTable 
                                equations={table.equations} 
                                tableTitle={table.name}
                            />
                        )
                    })}
                </Card.Section>
            </Card>
        </Layout.Section>
    )
}