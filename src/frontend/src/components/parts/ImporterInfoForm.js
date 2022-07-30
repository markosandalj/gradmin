import React from "react";
import { useDispatch } from "react-redux";

// COMPONENTS
import AutocompleteSelect from "./AutocompleteSelect"; 

// SHOPIFY
import { Form, FormLayout } from '@shopify/polaris';

// CONSTATNTS
import { allMaturasListApiRoute, SectionListApiRoute, SkriptaListApiRoute, SubjectListApiRoute } from "../../settings/apiRoutes";

// REDUX 
import { setSelectedMatura, setSelectedSection, setSelectedSkripta, setSelectedSubject } from "../../store/importerSlice";

export default function ImporterInfoForm() {
    const dispatch = useDispatch()

    const handleSubmit = (e) => {
        e.preventDefault();
    }

    return (
        <Form onSubmit={handleSubmit}>
            <FormLayout>
                <FormLayout.Group condensed>
                    <AutocompleteSelect 
                        apiUrl={allMaturasListApiRoute} 
                        label={'Matura'} 
                        setData={(data) => dispatch(setSelectedMatura(data))}
                    />
                    <AutocompleteSelect 
                        apiUrl={SubjectListApiRoute} 
                        label={'Subject'} 
                        setData={(data) => dispatch(setSelectedSubject(data))}
                    />
                </FormLayout.Group>
                <FormLayout.Group condensed>
                    <AutocompleteSelect 
                        apiUrl={SkriptaListApiRoute} 
                        label={'Skripta'} 
                        setData={(data) => dispatch(setSelectedSkripta(data))}
                    />
                    <AutocompleteSelect 
                        apiUrl={SectionListApiRoute} 
                        label={'Section'} 
                        setData={(data) => dispatch(setSelectedSection(data))}
                    />
                </FormLayout.Group>
            </FormLayout>
        </Form>
    )
}