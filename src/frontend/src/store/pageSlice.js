import { createSlice } from "@reduxjs/toolkit";

export const pageSlice = createSlice({
    name: "page",
    initialState: {
        isLoading: false,    
        userMenuOpen: false,
        isMobileNavigationActive: false,    
        pageTitle: 'Gradivo'
    },
    reducers: {
        toggleLoading: (state, { payload }) => {
            state.isLoading = !state.isLoading 
        },
        toggleUserMenu: (state, { payload }) => {
            state.userMenuOpen = !state.userMenuOpen 
        },
        toggleMobileNavigation: (state, { payload }) => {
            state.isMobileNavigationActive = !state.isMobileNavigationActive 
        }
    }
})


export const { toggleLoading, toggleUserMenu, toggleMobileNavigation } = pageSlice.actions;

export default pageSlice.reducer;