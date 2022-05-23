import * as actions from '../actions/actionTypes';

const CheatsheetReducer = (cheatsheet = {}, action) => {
    switch (action.type) {
        case actions.FETCH_CHEATSHEET:
            console.log('Data fetched: ', action.payload)
            return action.payload

        case actions.UPDATE_CHEATSHEET:
            
            return;

        case actions.UPDATE_EQUATION:
            const equations = [
                ...cheatsheet.cheatsheet_sections.map(section => section.equations),
                ...cheatsheet.cheatsheet_tables.map(table => table.equations),
            ].flat()
            
            const equation = {
                ...equations.find(eq => eq.id === action.payload.id),
                id: action.payload.id,
                equation : action.payload.equation
            }
            console.log('cheatsheet: ', equations, equation, cheatsheet)
            return {...cheatsheet}
            
        default:
            return cheatsheet
    }
}

export default CheatsheetReducer;