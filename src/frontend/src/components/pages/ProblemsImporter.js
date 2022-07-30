import React, {  useState, useCallback } from "react";
import axios from "axios";

// SHOPIFY
import { Layout, Button, ButtonGroup, DropZone, Spinner, Card } from '@shopify/polaris';

// COMPONENTS
import ImporterInfoForm from '../parts/ImporterInfoForm';
import ProblemsTable from "../parts/ProblemsTable";

// CONSTANTS
import { SUCCESS, CRITICAL } from "../../settings/constants";
import { importerApiRoute } from "../../settings/apiRoutes";

// REDUX
import { useDispatch, useSelector } from "react-redux";
import { closeBanner, showBanner } from "../../store/bannerSlice";
import { setUploadIsDone, setUploadInProgress, setItems } from "../../store/importerSlice";


export default function ProblemsImporter() {
    const dispatch = useDispatch()
    const { isUploadInProgress, isUploadDone, items } = useSelector(store => store.importer)
    const [file, setFile] = useState()

    const handleDropZoneDrop = useCallback(
        (_dropFiles, acceptedFiles, _rejectedFiles) =>
            setFile(file => acceptedFiles[0]),  
        [],
    );

    const handleUpload = async () => {
        dispatch(setUploadInProgress())

        let formData = new FormData();

        formData.append('file', file)

        const response = await axios.post(
                importerApiRoute, 
                formData,
                { headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"} }
            )
            .then(res => {
                return res.data
            })
            .then(data => {
                dispatch(setItems(data.map(item => ({ ...item, id: item.mathpix_response.request_id}))))
                dispatch(showBanner({ 
                        title: 'PDF uspješno uploadan. Bravo!',
                        status: SUCCESS
                    }))
            
                return data
            })
            .catch(err => {
                console.log(err);
                dispatch(showBanner({ 
                    title: "Nešto u pozadini je krepalo. Refreshaj stranicu i probaj opet!",
                    status: CRITICAL,
                    message: err
                }))
            })
            .finally(() => {
                dispatch(setUploadIsDone())
            })
    }

    const fileUpload = !file && <DropZone.FileUpload />;


    return (
        <Layout.Section>
            <Card 
                title="Problems importer"
                primaryFooterAction={{ 
                    content: "Upload", 
                    onClick: handleUpload,
                    loading: isUploadInProgress,
                    disabled: !file || isUploadDone
                }}
            >
                <Card.Section title="Upload PDF">
                    { isUploadInProgress ? 
                        <Spinner accessibilityLabel="Spinner example" size="large" />  
                            : 
                                <DropZone allowMultiple={false} onDrop={handleDropZoneDrop}>
                                    {fileUpload}
                                    {file && file.name}
                                </DropZone>}
                </Card.Section>
            </Card>
                                
            <Card title="Problems importer">
                <Card.Section title="Pick matura, section, skripta and subject">
                    <ImporterInfoForm />
                </Card.Section>
            </Card>
            <ProblemsTable items={items} />
        </Layout.Section>
    )
}