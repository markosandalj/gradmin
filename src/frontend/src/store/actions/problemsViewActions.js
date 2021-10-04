import * as actions from './actionTypes';

export const toggleEditingView = (editing = null) => ({
    type: actions.TOGGLE_EDITING,
    payload: {
        editing: editing
    }
})

export const togglePrintingView = (printing = null) => ({
    type: actions.TOGGLE_PRINT_PREVIEW,
    payload: {
        printing: printing
    }
})


export const toggleSitePreviewView = (site_preview = null) => ({
    type: actions.TOGGLE_SITE_PREVIEW,
    payload: {
        site_preview: site_preview
    }
})