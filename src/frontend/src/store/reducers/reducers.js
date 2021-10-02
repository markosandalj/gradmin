import { combineReducers } from 'redux';
import SkriptaReducer from './SkriptaReducer';
import ProblemsView from './problemsViewReducer';
import ProblemFieldsReducer from './problemFieldsReducer';

export default combineReducers ( {
    sections: SkriptaReducer,
    problems_view: ProblemsView,
    problem_fields: ProblemFieldsReducer,
});
