import { configureStore } from '@reduxjs/toolkit';
import importerReducer from './importerSlice'
import viewReducer from './viewSlice'
import bannerReducer from './bannerSlice';
import toastReducer from './toastSlice';
import saveBarReducer from './saveBarSlice';
import modalReducer from './modalSlice';
import pageReducer from './pageSlice.js';
import updateReducer from './updateSlice';

export const store = configureStore({
    reducer: {
        importer: importerReducer,
        view: viewReducer,
        banner: bannerReducer,
        toast: toastReducer,
        saveBar: saveBarReducer,
        modal: modalReducer,
        page: pageReducer,
        update: updateReducer
    },
})