// REACT & REDUX
import React from "react";
import { useParams } from 'react-router';

// SHOPIFY  
import { Layout, Card, ResourceList, ResourceItem, TextStyle } from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

// SETTINGS
import { maturaListApiRoute } from "../../settings/apiRoutes";

export const MaturaList = () => {
    const { subject_id } = useParams();
    const { data, loading, error } = useFetch(maturaListApiRoute(subject_id))

    if(loading) return <></> // remove and replace by loader inside useFetch hook

    const renderItem = (item) => {
        const { id, subject, term, year } = item
        const url = `/index/matura/${id}`
        const name = `${subject.subject_name} ${ subject.level !== '0' ? subject.level : '' } - ${year.year}. ${term.term}`

        return (
            <ResourceItem
              id={id}
              url={url}
              accessibilityLabel={`View details for ${name}`}
            >
              <h3>
                <TextStyle variation="strong">{name}</TextStyle>
              </h3>
            </ResourceItem>
          );
    }

    return (
        <Layout.AnnotatedSection title={`Popis svih matura`} >
            <Card>
                <ResourceList 
                    resourceName={{ singular: "Matura", plural: "Mature" }}
                    items={data}
                    renderItem={renderItem}
                />
            </Card>
        </Layout.AnnotatedSection>
    )
}