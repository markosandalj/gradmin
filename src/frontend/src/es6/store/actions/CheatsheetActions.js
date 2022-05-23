import * as actions from './actionTypes';
import * as api from '../api/api';

export const getCheatsheetData = (id) => async (dispatch) => {
    try {
        const {data} = await api.fetchCheatsheet(id);
        dispatch({ type: actions.FETCH_CHEATSHEET, payload: data })
    } catch(error) {
        console.log(error.message)
    }
}

export const updateEquation = (id, equation) => ({
    type: actions.UPDATE_EQUATION,
    payload: {
        id: id,
        equation: equation
    }
})