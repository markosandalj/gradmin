import React, { useState, useEffect } from "react";
import { useParams } from 'react-router';

// REDUX
import { useDispatch, useSelector } from "react-redux";
import { toggleEditingView, togglePrintPreviewView, toggleReviewView, toggleStandardView } from "../../store/viewSlice";

// SHOPIFY
import { Layout, Card, Stack, Button, ButtonGroup, DisplayText, Icon, ActionList } from '@shopify/polaris';
import { EditMinor, PrintMinor, BlockMinor, ToolsMajor } from '@shopify/polaris-icons';

// CUSTOM HOOKS
import useFetch from "../hooks/useFetch";
import { SkriptaSection } from "./SkriptaSection";

// SETTINGS
import { skriptaFullApiRoute } from "../../settings/apiRoutes";
import { REVIEW_VIEW_TYPE } from "../../settings/constants";

// UTILS
import { mathjaxTypeset } from "../../utils/mathjaxTypeset";

// COMPONENTS
import { SolutionsTable } from "../SolutionsTable";
import { FixedFullscreenBar } from "../FixedFullscreenBar";

export const Skripta = () => {
    const viewType = useSelector(store => store.view.viewType)
    const { skripta_id, section_id, section_order } = useParams();

    const { data, loading, error } = useFetch(skriptaFullApiRoute(skripta_id, section_id))
    
    const [sections, setSections] = useState(null)

    useEffect(() => {
        if(!data) return;
        
        setSections(section_id ? data : data.sections)
        console.log(section_id ? data : data.sections, section_id)

      return () => {
        setSections(null)
      }
    }, [data])

    const dispatch = useDispatch()


    if(!sections) return <></>;

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
        },
        {
            content: 'Print page',
            icon: PrintMinor, 
            onAction: () => console.log('TODO: print this page')
        }
    ]

    return (
        <>
            <FixedFullscreenBar>
                <Stack>
                    <Stack.Item fill>
                        <DisplayText size="small">Skripta</DisplayText>
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
                                    actions: pageActions
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
                    {sections.map((section, index) => {
                        return <SkriptaSection key={`skriptaSection-${section.id}`} section={section} sectionNumber={section_order} />
                    })}
                </div>
            </Layout.Section>
            <Layout.Section>
                {sections.map((section, index) => {
                    return (
                        <Card title="Tablica s rješenjima" nsTable key={`solutionTable-${section.id}`} >
                            <Card.Section>
                                <SolutionsTable section={section} sectionNumber={section_order} />
                            </Card.Section>
                        </Card>
                    )
                })}
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
//                 setDisplaySuccesAlert(true);
//                 console.log(`Successfully sent form data` + res.data);
//                 setDisplayDownloadModal(true)
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


// const handlePrint = () => {
//     if(!view.printing) handlePrintingToggle();
//     setDownloadLoading(!downloadLoading)
//     let apiUrl = `${window.location.origin}/api/skripta/print`;
//     let printElement = document.querySelector('#printThis')
    
//     let formData = new FormData();
//     formData.append('html', JSON.stringify(printElement.innerHTML) ) 
//     formData.append('id', skripta_id)
    
//     axios.post(
//         apiUrl,
//         formData,
//         {
//             headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"}
//         }
//     ).then(res => {
//         console.log(`Successfully sent form data`);
//         console.log(JSON.parse(res.data).file)
//         setDownloadLink(JSON.parse(res.data).file)
//         setDisplayDownloadModal(!displayDownloadModal)
//     })
//     .catch(err => {
//         console.log(err);
//         setDownloadLoading(!downloadLoading)
//         setDisplayDownloadModal(!displayDownloadModal)
//     })
//     setDownloadLoading(!downloadLoading)
// }