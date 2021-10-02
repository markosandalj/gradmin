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