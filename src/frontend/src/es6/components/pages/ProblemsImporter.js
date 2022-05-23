// REACT & REDUX
import React, { Component, useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

// SHOPIFY
import { Page, Layout, Button, ButtonGroup, DropZone, Spinner, Banner, Card } from '@shopify/polaris';

import ImporterInfoForm from '../parts/ImporterInfoForm';
import ProblemsTable from "../parts/ProblemsTable";


export default function ProblemsImporter() {
    const [file, setFile] = useState(false);
    const [errorMsg, setErrorMsg] = useState('');
    const [mathpixResposneData, setMathpixResponseData] = useState([]);
    const [isLoaderActive, setIsLoaderActive] = useState(false);
    const [showErrorBanner, setShowErrorBanner] = useState(false);
    const [showSuccesBanner, setShowSuccesBanner] = useState(false);
    const [isCheckingProcessActive, setIscheckingProcessActive] = useState(false);
    const [info, setInfo] = useState( { matura: '', subject: '', section: '', skripta: '' } )

    const handleDropZoneDrop = useCallback(
        (_dropFiles, acceptedFiles, _rejectedFiles) =>
            setFile((file) => acceptedFiles[0]),  
        [],
    );

    const toggleCheckingProcess = () => {
        setIscheckingProcessActive(!isCheckingProcessActive)
    }

    const showDropZone = () => {
        return (!isLoaderActive && !showSuccesBanner && !showErrorBanner)
    }

    const handleUpload = async (event) => {
        event.preventDefault();
        setIsLoaderActive(true)

        let data = new FormData();

        data.append('file', file)

        const response = await axios.post(
                window.location.origin + '/api/problems_importer', 
                data,
                { headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"} }
            )
            .then(res => {
                return res.data
            })
            .then(data => {
                setIsLoaderActive(false)
                setShowSuccesBanner(true)
                setMathpixResponseData(data)
                toggleCheckingProcess()
                
                return data
            })
            .catch(err => {
                console.log(err);
                setErrorMsg(err);
                setShowErrorBanner(true)
            })   
    }

    const fileUpload = !file && <DropZone.FileUpload />;


    return (
        <Page>
            <Layout>
                <Layout.Section>
                    { showSuccesBanner &&
                        <div className="my-2">
                            <Banner
                                title="PDF uspješno uploadan. Bravo!"
                                status="success"
                            />
                        </div>}

                    { showErrorBanner &&
                        <div className="my-2">
                            <Banner
                                title="Nešto u pozadini je krepalo. Refreshaj stranicu i probaj opet!"
                                status="critical"
                            >
                                <p>
                                    {errorMsg}
                                </p>
                            </Banner>
                        </div>}

                    { !isCheckingProcessActive &&
                        <Card title="Problems importer">
                            <Card.Section title="Upload PDF">
                                { showDropZone() && 
                                    <DropZone allowMultiple={false} onDrop={handleDropZoneDrop}>
                                        {fileUpload}
                                        {file && file.name}
                                    </DropZone>}
                                { isLoaderActive && 
                                    <Spinner accessibilityLabel="Spinner example" size="large" /> }
                                    <div className="py-2 flex-end">
                                        <ButtonGroup>
                                            <Button primary onClick={handleUpload} loading={isLoaderActive} disabled={!file || showSuccesBanner}>Upload</Button>
                                        </ButtonGroup>
                                    </div>
                            </Card.Section>
                        </Card>}
                        
                        { isCheckingProcessActive && 
                            <>
                                <Card title="Problems importer">
                                    <Card.Section title="Upload PDF">
                                        <ImporterInfoForm setInfo={setInfo}></ImporterInfoForm>
                                    </Card.Section>
                                </Card>
                                <ProblemsTable problems={mathpixResposneData} info={info}></ProblemsTable>
                            </>}
                </Layout.Section>
            </Layout>
        </Page>
    )
}