import * as actions from './actionTypes';
import * as api from '../api/api';


export const getMaturaList = (subject_id) => async (dispatch) => {
    try {
        const {data} = await api.fetchMaturaList(subject_id);
        dispatch({ type: actions.FETCH_MATURA_LIST, payload: data })
    } catch(error) {
        console.log(error.message)
    }
}


export const getMaturaProblems = (matura_id) => async (dispatch) => {
    try {
        const {data} = await api.fetchMaturaProblems(subject_id);
        dispatch({ type: actions.FETCH_MATURA_PROBLEMS, payload: data })
    } catch(error) {
        console.log(error.message)
    }
}