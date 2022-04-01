import React, { Component, useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

// SHOPIFY
import { Form, FormLayout, Button } from '@shopify/polaris';

import AutocompleteSelect from "./AutocompleteSelect";

export default function ImporterInfoForm({formData, setFormData}) {
    const [matura, setMatura] = useState();
    const [subject, setSubject] = useState()
    const [section, setSection] = useState();
    const [skripta, setSkripta] = useState();

    const handleSubmit = (event) => {
        event.preventDefault();
        
        setFormData({
            ...formData,
            matura: matura,
            subject: subject,
            section: section,
            skripta: skripta,
        });
    }

    return (
        <Form onSubmit={handleSubmit}>
            <FormLayout>
                <FormLayout.Group condensed>
                    <AutocompleteSelect apiUrl={`/api/matura/all`} label={'Matura'} setData={setMatura}></AutocompleteSelect>
                    <AutocompleteSelect apiUrl={`/api/subject/all`} label={'Subject'} setData={setSubject}></AutocompleteSelect>
                </FormLayout.Group>
                <FormLayout.Group condensed>
                    <AutocompleteSelect apiUrl={`/api/section/all`} label={'Section'} setData={setSection}></AutocompleteSelect>
                    <AutocompleteSelect apiUrl={`/api/skripta/all`} label={'Skripta'} setData={setSkripta}></AutocompleteSelect>
                </FormLayout.Group>
                <Button submit>Save</Button>
            </FormLayout>
        </Form>
    )
}