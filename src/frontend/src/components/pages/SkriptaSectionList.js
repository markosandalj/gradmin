// REACT & REDUX
import React, { useState, useEffect } from "react";
import { useParams } from 'react-router';
import { Link } from "react-router-dom";

// SHOPIFY  
import { Layout, Card, ResourceList, ResourceItem, TextStyle } from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

// SETTINGS
import { SkriptaSectionListApiRoute } from "../../settings/apiRoutes";

export const SkriptaSectionList = () => {
    const { skripta_id } = useParams();
    const { data, loading, error } = useFetch(SkriptaSectionListApiRoute(skripta_id))
    const [skripta, setSkripta] = useState(null)
    const [name, setName] = useState('Skripta')

    useEffect(() => {
        if(!data) return;

        setName(data[0].name)
        setSkripta(data[0])

        return () => {
            setName('Skripta')
            setMatura({})
        }
    }, [data])

    

    const renderItem = (item, itemId, index) => {
        const { id, name } = item
        const url = `/index/skripta/${skripta.id}/${id}/${index+1}`

        return (
            <ResourceItem
              id={id}
              url={url}
              accessibilityLabel={`View details for ${name}`}
            >
              <h3>
                <TextStyle variation="strong">{index+1}. {name}</TextStyle>
              </h3>
            </ResourceItem>
          );
    }

    if(!skripta) return <></>

    return (
        <Layout.AnnotatedSection title={name} >
            <Card>
                <ResourceItem
                    id={skripta_id}
                    url={'/index/skripta/'+skripta_id}
                >
                    <h3>
                        <TextStyle variation="strong">Cijela skripta</TextStyle>
                    </h3>
                </ResourceItem>
                <ResourceList 
                    resourceName={{ singular: "Gradivo", plural: "Gradiva" }}
                    items={skripta.sections}
                    renderItem={renderItem}
                />
            </Card>
        </Layout.AnnotatedSection>
    )
}