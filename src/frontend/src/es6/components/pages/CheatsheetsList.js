// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { Link } from "react-router-dom";
import axios from 'axios'

// SHOPIFY
import { Page, Layout, Card, ResourceList, ResourceItem, TextStyle, Badge, SkeletonBodyText } from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

const CheatsheetsList = () => {
    const apiUrl = `${window.location.origin}/api/cheatsheets/list`
    const { data, loading, error } = useFetch(apiUrl)

    if (loading) return <SkeletonBodyText />; 
    if (error) return "Error!"; 

    const renderItem = (item) => {
        const { id, name, subject } = item;
        return (
            <ResourceItem id={id} url={`${window.location.origin}/index/cheatsheets/${id}`}>
                <div className="flex-space-between">
                    <h3>
                        <TextStyle variation="strong">{name}</TextStyle>
                    </h3>
                    <Badge>{subject.name}</Badge>
                </div>
            </ResourceItem>
          );
    }

    return (
        <Page>
            <Layout>
                <Layout.Section>
                    <Card>
                        <ResourceList
                            resourceName={{singular: 'Cheatsheet', plural: 'Cheatsheets'}}
                            items={data}
                            renderItem={renderItem}
                        >
                        </ResourceList>
                    </Card>
                </Layout.Section>
            </Layout>
        </Page>
    )
}

export default CheatsheetsList;