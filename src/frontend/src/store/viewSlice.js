import { createSlice } from "@reduxjs/toolkit";
import { EDITING_VIEW_TYPE, PRINT_PREVIEW_VIEW_TYPE, REVIEW_VIEW_TYPE, STANDARD_VIEW_TYPE } from "../settings/constants";



export const viewSlice = createSlice({
    name: "view",
    initialState: {
        viewType: STANDARD_VIEW_TYPE
    },
    reducers: {
        toggleView: (state, { payload }) => {
            state.viewType = payload
        },
        toggleStandardView: (state) => {
            state.viewType = STANDARD_VIEW_TYPE
        },
        toggleEditingView: (state) => {
            state.viewType = EDITING_VIEW_TYPE
        },
        togglePrintPreviewView: (state) => {
            state.viewType = PRINT_PREVIEW_VIEW_TYPE
        },
        toggleReviewView: (state) => {
            state.viewType = REVIEW_VIEW_TYPE
        }
    }
})

export const {
    toggleView,
    toggleStandardView,
    toggleEditingView,
    togglePrintPreviewView,
    toggleReviewView
} = viewSlice.actions;

export default viewSlice.reducer;