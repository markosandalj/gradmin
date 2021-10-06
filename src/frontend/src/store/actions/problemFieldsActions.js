import * as actions from './actionTypes';

export const addImage = (image, id) => ({
    type: actions.UPDATE_IMAGE_FIELDS,
    payload: {
        id,
        image: image
    }
})

export const addQuestion = (question_text, id) => ({
    type: actions.UPDATE_QUESTION_FIELDS,
    payload: {
        id: id,
        question_text: question_text
    }
})

export const addAnswerChoice = (choice_text, id) => ({
    type: actions.UPDATE_ANSWER_CHOICE_FIELDS,
    payload: {
        id: id,
        choice_text: choice_text
    }
})

export const approveProblem = (approval, id) => ({
    type: actions.APPROVE_PROBLEM,
    payload: {
        id: id,
        approval: approval
    }
})