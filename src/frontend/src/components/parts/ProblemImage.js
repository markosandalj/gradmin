import React from "react";

// SHOPIFY
import { Stack } from '@shopify/polaris';

// COMPONENTS
import { EditableImageField } from "../EditableImageField";

// SETTINGS
import { PRINT_PREVIEW_VIEW_TYPE } from "../../settings/constants";

// REDUX
import { useSelector } from "react-redux";

export const ProblemImage = ({ image }) => {
    const viewType = useSelector(store => store.view.viewType)
    
    if(!image) return <></>;

    return (
        <Stack distribution="fillEvenly">
            <EditableImageField 
                id={image.id}
                image={image.image}
            />
            {viewType !== PRINT_PREVIEW_VIEW_TYPE && 
                <EditableImageField 
                    id={image.id}
                    image={image.image_dark}
                />}
        </Stack>
    )
}