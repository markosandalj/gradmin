import * as actions from './actionTypes';
import * as api from '../api/api';

export const getProblems = (skripta_id, section_id) => async (dispatch)  => {
    try {
        const { data } = await api.fetchProblems(skripta_id, section_id);
        dispatch({ type: actions.FETCH_SKRIPTA_PROBLEMS, payload: data })
    } catch(error) {
        console.log(error.message)
    }
}

export const updateQuestionText = (problem_id, question_text) => ({
    type: actions.UPDATE_QUESTION_TEXT,
    payload: {
        section_id: section_id,
        problem_id: problem_id,
        question_text: question_text,
    }
})

export const updateSubquestionText = (problem_id, subquestion_id, subquestion_text) => ({
    type: actions.UPDATE_SUBQUESTION_TEXT,
    payload: {
        section_id: section_id,
        problem_id: problem_id,
        subquestion_id: subquestion_id,
        subquestion_text: subquestion_text,
    }
})

export const updateQuestionImage = (problem_id, question_image) => ({
    type: actions.UPDATE_QUESTION_IMAGE,
    payload: {
        section_id: section_id,
        problem_id: problem_id,
        question_image: question_image,
    }
})

export const updateAnswerChoiceText = (problem_id, answer_choice_id, answer_choice_text) => ({
    type: actions.UPDATE_ANSWER_CHOICE_TEXT,
    payload: {
        section_id: section_id,
        problem_id: problem_id,
        answer_choice_id: answer_choice_id,
        answer_choice_text: answer_choice_text
    }
})

export const updateAnswerChoiceImage = (problem_id, answer_choice_id, answer_choice_image) => ({
    type: actions.UPDATE_ANSWER_CHOICE_IMAGE,
    payload: {
        section_id: section_id,
        problem_id: problem_id,
        answer_choice_id: answer_choice_id,
        answer_choice_image: answer_choice_image
    }
})

export const updateProblemOrder = (problem_id, order) => ({
    type: actions.UPDATE_PROBLEM_ORDER,
    payload: {
        section_id: section_id,
        problem_id: problem_id,
        order: order
    }
})

