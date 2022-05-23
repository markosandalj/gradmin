// REACT & REDUX
import React, { useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";

// SHOPIFY
import {Page, Layout, SkeletonBodyText, Card, Stack, ButtonGroup, Button, Heading } from '@shopify/polaris'; 

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faList, faPen, faSearchPlus, faTools, faTimes } from '@fortawesome/free-solid-svg-icons'

// HELPERS
import { typsetMathjax } from "../helpers/typsetMathjax";
import handlePrint from '../helpers/handlePrint'


// ACTIONS
import { toggleEditingView } from "../../store/actions/pageViewActions";
import { togglePrintPreviewView } from "../../store/actions/pageViewActions";

const PageActions =({ title, viewTypeSwitcher }) => {
    const { cheatsheet_id } = useParams() 
    const [isFirstButtonActive, setIsFirstButtonActive] = useState(true);
    const [printLoader, setPrintLoader] = useState(false);
    const [downloadLink, setDownloadLink] = useState(null)

    const dispatch = useDispatch()
    const state =  useSelector( (state) => state )
    const view = useSelector( state => state.view )

    const handleFirstButtonClick = useCallback(() => {
        if (isFirstButtonActive) return;
        dispatch(togglePrintPreviewView());
        setIsFirstButtonActive(true);
    }, [isFirstButtonActive]);

    const handleSecondButtonClick = useCallback(() => {
        if (!isFirstButtonActive) return;
        dispatch(toggleEditingView())
        setIsFirstButtonActive(false)
    }, [isFirstButtonActive]);

    const handlePrintFn = async () => {
        setPrintLoader(true);
        dispatch(togglePrintPreviewView());
        await typsetMathjax();
        const data = await handlePrint('#printThis', title, cheatsheet_id);
        console.log(typeof data)
        setDownloadLink(data.file)
        setPrintLoader(false)
    }

    return (
        <Layout.Section>
            <Stack>
                <Stack.Item fill>
                    <Heading>{title}</Heading>
                </Stack.Item>
                <Stack.Item>
                    <ButtonGroup>
                        <ButtonGroup segmented>
                            <Button pressed={isFirstButtonActive} onClick={handleFirstButtonClick}>Print preview</Button>
                            <Button pressed={!isFirstButtonActive} onClick={handleSecondButtonClick}>Editing</Button>
                        </ButtonGroup>
                        <Button
                            primary
                            connectedDisclosure={{
                                accessibilityLabel: 'Other save actions',
                                actions: [{content: 'Typset LaTeX', onAction: typsetMathjax }, {content: 'Print', onAction: () => handlePrintFn() }],
                            }}
                        >
                            Save
                        </Button>
                    </ButtonGroup>
                </Stack.Item>
            </Stack>
            {(printLoader || downloadLink) && 
                <Stack>
                    <Button 
                        external 
                        url={downloadLink} 
                        loading={printLoader} 
                        fullWidth 
                        primary>Download</Button>
                </Stack>}
        </Layout.Section>
    );
}
  
export default PageActions;