import * as actions from './actionTypes';

export const toggleEditingView = (view = 'editing') => ({
    type: actions.TOGGLE_EDITING,
    payload: {
        view: view
    }
})

export const togglePrintPreviewView = (view = 'print_preview') => ({
    type: actions.TOGGLE_PRINT_PREVIEW,
    payload: {
        view: view
    }
})


export const toggleSitePreviewView = (view = 'standard') => ({
    type: actions.TOGGLE_SITE_PREVIEW,
    payload: {
        view: view
    }
})