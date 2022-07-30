import React from 'react'

// SHOPIFY
import { Button, ButtonGroup } from '@shopify/polaris';

// REDUX
import { useDispatch, useSelector } from 'react-redux';
import { toggleEditingView, togglePrintPreviewView, toggleStandardView } from '../store/viewSlice';

// CONSTANTS
import { EDITING_VIEW_TYPE, PRINT_PREVIEW_VIEW_TYPE, STANDARD_VIEW_TYPE } from '../settings/constants';

export const ViewSwitcher = ({ edit, print }) => {
    const { viewType } = useSelector(store => store.view)
    const dispatch = useDispatch()

    if(!print && !edit) return;

    return (
        <ButtonGroup segmented>
            <Button outline pressed={viewType === STANDARD_VIEW_TYPE} onClick={() => dispatch(toggleStandardView())}>Standard</Button>
            {edit && <Button outline pressed={viewType === EDITING_VIEW_TYPE} onClick={() => dispatch(toggleEditingView())}>Edit</Button>}
            {print && <Button outline pressed={viewType === PRINT_PREVIEW_VIEW_TYPE} onClick={() => dispatch(togglePrintPreviewView())}>Print preview</Button>}
        </ButtonGroup>
    )
}
