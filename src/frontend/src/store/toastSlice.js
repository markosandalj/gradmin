import { createSlice } from "@reduxjs/toolkit";

export const toastSlice = createSlice({
    name: "toast",
    initialState: {
        isActive: false,
        content: 'Banner',
        error: false,
        duration: 800,
    },
    reducers: {
        showToast: (state, { payload }) => {
            state.isActive = true
            state.content = payload.content || ''
            state.error = payload.error
        },
        closeToast: (state) => {
            state.isActive = false
            state.content = ''
            state.error = false
        },
    }
})


export const { showToast, closeToast } = toastSlice.actions;

export default toastSlice.reducer;