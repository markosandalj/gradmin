import { createSlice } from "@reduxjs/toolkit";

export const modalSlice = createSlice({
    name: "modal",
    initialState: {
        isOpen: false,
        title: 'Modal',
    },
    reducers: {
        showModal: (state, { payload }) => {
            state.isOpen = true
            state.title = payload.title || ''
        },
        closeModal: (state) => {
            state.isOpen = false
            state.title = ''
        },
    }
})


export const { showModal, closeModal } = modalSlice.actions;

export default modalSlice.reducer;