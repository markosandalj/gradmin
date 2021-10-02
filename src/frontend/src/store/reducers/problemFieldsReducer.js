import * as actions from '../actions/actionTypes';

const ProblemFieldsReducer = (problem_fields = {}, action) => {
    switch (action.type) {
        case actions.UPDATE_IMAGE_FIELDS:
            if(problem_fields.images) {
                let imageIndex = problem_fields.images.findIndex( image => image.id === action.payload.id )
                let image = imageIndex ? problem_fields.images[imageIndex] : null;
                if(imageIndex && image) {
                    problem_fields.images.splice(imageIndex, 1, action.payload)
                } else {
                    problem_fields.images.push(action.payload)
                }
            } else {
                problem_fields.images = []
                problem_fields.images.push(action.payload)
            }
            return {...problem_fields}
        case actions.UPDATE_QUESTION_FIELDS:
            if(problem_fields.questions) {
                let questionIndex = problem_fields.questions.findIndex(question => question.id === action.payload.id )
                let question = problem_fields.questions.find(question => question.id === action.payload.id)
                if(question) {
                    problem_fields.questions.splice(questionIndex, 1, action.payload)
                } else {
                    problem_fields.questions.push(action.payload)
                }
            } else {
                problem_fields.questions = []
                problem_fields.questions.push(action.payload)
            }
            return {...problem_fields}
        case actions.UPDATE_ANSWER_CHOICE_FIELDS:
            if(problem_fields.answer_choices) {
                let answerChoiceIndex = problem_fields.answer_choices.findIndex(answer_choice => answer_choice.id === action.payload.id )
                let answer_choice = problem_fields.answer_choices.find(answer_choice => answer_choice.id === action.payload.id)
                if(answer_choice) {
                    problem_fields.answer_choices.splice(answerChoiceIndex, 1, action.payload)
                } else {
                    problem_fields.answer_choices.push(action.payload)
                }
            } else {
                problem_fields.answer_choices = []
                problem_fields.answer_choices.push(action.payload)
            }
            return {...problem_fields}
        default:
            return problem_fields
    }
}

export default ProblemFieldsReducer;