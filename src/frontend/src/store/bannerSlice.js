import { createSlice } from "@reduxjs/toolkit";

export const bannerSlice = createSlice({
    name: "banner",
    initialState: {
        isOpen: false,
        status: '', // warning || info || succes || critical
        title: 'Banner',
        message: ''
    },
    reducers: {
        showBanner: (state, { payload }) => {
            state.isOpen = true
            state.status = payload.status || ''
            state.title = payload.title || ''
            state.message = payload.message || ''
        },
        closeBanner: (state) => {
            state.isOpen = false
            state.status = ''
            state.title = ''
            state.message = ''
        },
    }
})


export const { showBanner, closeBanner } = bannerSlice.actions;

export default bannerSlice.reducer;