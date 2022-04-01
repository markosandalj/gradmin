// REACT & REDUX
import React, { Component, useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

// SHOPIFY
import { Page, Layout, Button, ButtonGroup, DropZone, Spinner, Banner, Card } from '@shopify/polaris';

import ImporterInfoForm from '../parts/ImporterInfoForm';
import ImageProblemsChecker from "../parts/ImageProblemChecker";


export default function ProblemsImporter() {
    const [file, setFile] = useState(false);
    const [errorMsg, setErrorMsg] = useState('');
    const [mathpixResposneData, setMathpixResponseData] = useState([]);
    const [activeImage, setActiveImage] = useState({});
    const [isLoaderActive, setIsLoaderActive] = useState(false);
    const [showErrorBanner, setShowErrorBanner] = useState(false);
    const [showSuccesBanner, setShowSuccesBanner] = useState(false);
    const [isCheckingProcessActive, setIscheckingProcessActive] = useState(false);
    const [formData, setFormData] = useState();

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

    const handleSubmit = async (event) => {
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
                setActiveImage(data[0])
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
                    { !isCheckingProcessActive &&
                        <Card title="Problems importer">
                            <Card.Section title="Upload PDF">
                                {showErrorBanner &&
                                    <Banner
                                        title="Nešto u pozadini je kraplo. refreshaj stranicu i probaj opet!"
                                        status="critical"
                                    >
                                        <p>
                                            {errorMsg}
                                        </p>
                                    </Banner>}
                                {showSuccesBanner &&
                                    <Banner
                                        title="PDF uspješno uploadan. Bravo!"
                                        status="success"
                                        action={{onAction: toggleCheckingProcess, content: "Kreni s provjerom"}}
                                    >
                                        <p>
                                            "PDF uspješno uploadan i procesiran. Ispuni formu s podatcim koji će se primjeniti na sve zadatke u ovom pdf-u."
                                        </p>
                                    </Banner>}
                                {showSuccesBanner &&
                                    <ImporterInfoForm formData={formData} setFormData={setFormData}></ImporterInfoForm>
                                }
                                { showDropZone() && 
                                    <DropZone allowMultiple={false} onDrop={handleDropZoneDrop}>
                                        {fileUpload}
                                        {file && file.name}
                                    </DropZone>}
                                { isLoaderActive && 
                                    <Spinner accessibilityLabel="Spinner example" size="large" /> }
                                    <div className="py-2 flex-end">
                                        <ButtonGroup>
                                            <Button primary onClick={handleSubmit} loading={isLoaderActive} disabled={!file || showSuccesBanner}>Upload</Button>
                                        </ButtonGroup>
                                    </div>
                            </Card.Section>
                        </Card>}
                        
                        { isCheckingProcessActive && 
                            <ImageProblemsChecker mathpixResposneData={mathpixResposneData} activeImage={activeImage} setActiveImage={setActiveImage} formData={formData} setFormData={setFormData}></ImageProblemsChecker>
                        }
                </Layout.Section>
            </Layout>
        </Page>
    )
}