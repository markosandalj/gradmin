import { combineReducers } from 'redux';
import SkriptaReducer from './SkriptaReducer';
import PageViewReducer from './pageViewReducer';
import ProblemFieldsReducer from './problemFieldsReducer';
import CheatsheetReducer from './CheatsheetReducer';

export default combineReducers ( {
    sections: SkriptaReducer,
    view: PageViewReducer,
    problem_fields: ProblemFieldsReducer,
    cheatsheet: CheatsheetReducer,
});
