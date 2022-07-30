import { createSlice } from "@reduxjs/toolkit";

export const saveBarSlice = createSlice({
    name: "saveBar",
    initialState: {
        isActive: false,
        message: '',
        saveAction: null, // should probably change to api url and have one function/hook that will handle the upload
        discardAction: null,
        apiUrl: null,
    },
    reducers: {
        showSaveBar: (state, { payload }) => {
            state.isActive = true
            state.message = payload?.message ?? ''
            state.apiUrl = payload?.apiUrl ?? null
        },
        closeSaveBar: (state) => {
            state.isActive = false
            state.message = ''
        },
    }
})


export const { showSaveBar, closeSaveBar } = saveBarSlice.actions;

export default saveBarSlice.reducer;