// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { useParams } from 'react-router';
import { Link } from "react-router-dom";
import axios from 'axios'

// SHOPIFY
import { Page, Layout, Card, ResourceList, ResourceItem, TextStyle, Badge, SkeletonBodyText, Stack } from '@shopify/polaris';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

// SETTINGS
import { cheatsheetsListApiRoute } from "../../settings/apiRoutes";

export const CheatsheetsList = () => {
    const { data, loading, error } = useFetch(cheatsheetsListApiRoute)
    
    if (loading) return <SkeletonBodyText />; 
    if (error) return "Error!"; 


    const renderItem = (item) => {
        const { id, name, subject } = item;

        return (
            <ResourceItem id={id} url={`${window.location.origin}/index/cheatsheets/${id}`}>
                <Stack>
                    <Stack.Item fill>
                        <h3>
                            <TextStyle variation="strong">{name}</TextStyle>
                        </h3>
                    </Stack.Item>
                    <Stack.Item>
                        <Badge>{subject.name}</Badge>
                    </Stack.Item>
                </Stack>
            </ResourceItem>
          );
    }

    return (
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
    )
}