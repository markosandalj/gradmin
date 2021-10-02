import * as actions from '../actions/actionTypes';

const problemsBySectionReducer = (sections = [], action) => {
    if(sections.lenght > 0) {
        let payload = action?.payload
        let section_id = payload?.section_id
        let problems = sections.find(section => section.id === section_id)?.problems
        let problem_id = payload?.problem_id
        let problem = problems.find(problem => problem.id === problem_id)
        let index = problems.findIndex(problem => problem.id === problem_id)
    }
    
    switch (action.type) {
        case actions.FETCH_PROBLEMS:
            console.log(action.payload)
            return action.payload[0].sections ? action.payload[0].sections : action.payload;
        case actions.UPDATE_QUESTION_TEXT:
            problem.question.question_text = payload.question_text
            return problems.splice(index, 1, problem)  ? problems.splice(index, 1, problem) : problems;
        case actions.UPDATE_QUESTION_IMAGE:
            return sections;
        case actions.UPDATE_SUBQUESTION_TEXT:
            return sections;
        case actions.UPDATE_ANSWER_CHOICE_TEXT:
            let answer_choice = problem.answer_choices.find(choice => choice.id === payload.answer_choice_id)
            let answer_choice_index = problem.answer_choices.findIndex(choice => choice.id === payload.answer_choice_id)
            problem.answer_choices.splice(answer_choice_index, 1, answer_choice)
            return problems.splice(index, 1, problem) ? problems.splice(index, 1, problem) : problems;
        case actions.UPDATE_ANSWER_CHOICE_IMAGE:
            return sections;
        case actions.UPDATE_PROBLEM_ORDER:
            return sections;
        default:
            return sections
    }
}

export default problemsBySectionReducer;