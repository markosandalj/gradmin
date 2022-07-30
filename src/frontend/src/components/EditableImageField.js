import React, { useState, useCallback } from 'react'

// SHOPIFY
import { Stack, DropZone, Thumbnail, Icon, Caption } from '@shopify/polaris'
import { EditMinor, ImageMajor } from "@shopify/polaris-icons";

// REDUX 
import { useDispatch, useSelector } from 'react-redux'

// SETTINGS
import { EDITING_VIEW_TYPE } from '../settings/constants'

// UTILS
import { mathjaxTypeset } from '../utils/mathjaxTypeset'

// COMPONENTS
import { FloatingEditButton } from './FloatingEditButton';
import { addImageToUpdateQueue } from '../store/updateSlice';
import { showSaveBar } from '../store/saveBarSlice';


export const EditableImageField = ({ id, image, relatedItemId }) => {
    const dispatch = useDispatch()

    const { viewType } = useSelector(store => store.view)
    const [hasChanged, setHasChanged] = useState(false)
    const [isOpen, setIsOpen] = useState(false)
    const [files, setFiles] = useState([image]);


    const validFileTypes = ["image/gif", "image/jpeg", "image/png"];

    const toggleField = () => {
        setIsOpen(!isOpen)

        if(hasChanged) mathjaxTypeset();
    }

    const fileUpload = !files.length && <DropZone.FileUpload />;

    const handleDropZoneDrop = useCallback(
        (_dropFiles, acceptedFiles, _rejectedFiles) => {
            setFiles((files) => [...acceptedFiles])
            dispatch(addImageToUpdateQueue({ id: id, images: [...acceptedFiles], relatedItemId: relatedItemId }))
            setHasChanged(true)
            dispatch(showSaveBar({ message: 'Save all changes'}))
        }
    , []);

    const uploadedFiles = files.length > 0 && (
        <div style={{ padding: "0" }}>
            <Stack vertical>
                {files.map((file, index) => (
                    <Stack alignment="center" key={index}>
                        <Thumbnail
                            size="small"
                            alt={file.name}
                            source={
                                validFileTypes.includes(file.type)
                                ? window.URL.createObjectURL(file)
                                : ImageMajor
                            }
                        />
                        <div>
                            <Caption>{file.name}</Caption>
                        </div>
                    </Stack>
                ))}
            </Stack>
        </div>
    );

    if(!image) return <></>;
    
    return (
        <>
            <Stack wrap={false}>
                <Stack.Item fill>
                    <Thumbnail source={image} size="large" />
                </Stack.Item>
                <Stack.Item>
                    {viewType === EDITING_VIEW_TYPE &&
                        <FloatingEditButton onClick={toggleField}>
                            <Icon source={EditMinor} />
                        </FloatingEditButton>}
                </Stack.Item>
            </Stack>
            {viewType === EDITING_VIEW_TYPE && isOpen &&
                <DropZone onDrop={handleDropZoneDrop}>
                    {uploadedFiles}
                    {fileUpload}
                </DropZone>
            }
        </>
    )
}
