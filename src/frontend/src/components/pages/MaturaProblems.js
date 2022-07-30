
// REACT & REDUX
import React, { useState, useEffect } from "react";
import { useParams } from 'react-router';
import axios from 'axios'

// SHOPIFY
import { Layout, Stack, Button, ButtonGroup, Card, DisplayText, Icon } from '@shopify/polaris';
import { EditMinor, PrintMinor, BlockMinor, ToolsMajor } from '@shopify/polaris-icons';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";

// COMPONENTS
import { Problem } from "../parts/Problem";
import { FixedFullscreenBar } from "../FixedFullscreenBar";

// SETTINGS
import { MaturaFullApiRoute } from "../../settings/apiRoutes";
import { REVIEW_VIEW_TYPE } from "../../settings/constants";

// REDUX
import { useDispatch, useSelector } from "react-redux";
import { toggleStandardView, toggleEditingView, togglePrintPreviewView, toggleReviewView } from '../../store/viewSlice'

// UTILS
import { mathjaxTypeset } from '../../utils/mathjaxTypeset'

export const MaturaProblems = () => {
    const dispatch = useDispatch()
    const { matura_id } = useParams();
    const { data, loading, error } = useFetch(MaturaFullApiRoute + matura_id)
    const [name, setName] = useState('Matura')
    const [matura, setMatura] = useState({})
    const viewType = useSelector(store => store.view.viewType)

    useEffect(() => {
        if(!data) return;
    
        const { subject, year, term } = data[0]
        setName(`${subject.subject_name} ${ subject.level !== '0' ? subject.level : '' } - ${year.year}. ${term.term}`)
        setMatura(data[0])

        return () => {
            setName('Matura')
            setMatura({})
        }
    }, [data])

    const pageActions = [
        {
            content: 'Edit',
            icon: EditMinor,
            onAction: () => dispatch(toggleEditingView())
        },
        {
            content: 'Print preview',
            icon: PrintMinor, 
            onAction: () => dispatch(togglePrintPreviewView())
        },
        {
            content: 'Standard view',
            icon: BlockMinor,
            onAction: () => dispatch(toggleStandardView())
        }
    ]
    
    
    if (loading) return <></>; 
    if (error) return "Error!"; 

    return (
        <>
            <FixedFullscreenBar>
                <Stack>
                    <Stack.Item fill>
                        <DisplayText size="small">{name}</DisplayText>
                    </Stack.Item>
                    <Stack.Item>
                        <ButtonGroup>
                            <Button
                                onClick={() => dispatch(toggleReviewView())}
                                pressed={viewType === REVIEW_VIEW_TYPE}
                            >
                                Review
                            </Button>
                            <Button
                                connectedDisclosure={{
                                    accessibilityLabel: "Other actions",
                                    actions: pageActions,
                                }}
                                onClick={mathjaxTypeset}
                                icon={ToolsMajor}
                            >
                                Fix math
                            </Button>
                        </ButtonGroup>
                    </Stack.Item>
                </Stack>
            </FixedFullscreenBar>
            <Layout.Section>
                <div style={{paddingTop: '5.5rem'}}>
                    {matura?.problems?.map( (problem, index) => {
                        return (
                            <Card key={problem.id} sectioned>
                                <Problem 
                                    key={problem.id}
                                    problem={problem}
                                />
                            </Card>
                        )
                    })}
                </div>
            </Layout.Section>
        </>
    )
}

// const handleSubmit = (event) => {
//     event.preventDefault();

//     if(Object.keys(problem_fields).length > 0) {
//         let formData = new FormData();
        
//         for(const [key, value] of Object.entries(problem_fields)){
//             formData.append(key, JSON.stringify(value) )
//         };
//         console.log(...formData)
//         let apiUrl = window.location.origin + '/api/question/update';
//         axios.post(
//                 apiUrl,
//                 formData,
//                 {
//                     headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"}
//                 }
//             ).then(res => {                    
//                 console.log(`Successfully sent form data` + res.data);
//             }).then(() => {
//                 dispatch(showBanner({
//                     status: SUCCESS,
//                     title: 'Podatci uspješno spremljeni u bazu!',

//                 }))
//             })
//             .catch(err => {
//                 console.log(err);
//                 setDisplayErrorAlert(true)
//             })
//     } else {
//         console.log(problem_fields)
//         console.log(state)
//         console.log('Empty')
//     }
// }