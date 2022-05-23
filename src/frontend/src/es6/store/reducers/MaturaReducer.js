import * as actions from '../actions/actionTypes';

const MaturaReducer = ( matura = {}, action) => {
    switch (action.type) {
        case actions.FETCH_MATURA_PROBLEMS:
            return action.payload[0].matura ? action.payload[0].matura : action.payload;
        default:
            return matura
    }
}