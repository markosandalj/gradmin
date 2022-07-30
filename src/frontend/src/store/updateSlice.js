import { createSlice } from "@reduxjs/toolkit";

export const updateSlice = createSlice({
    name: "update",
    initialState: {
        problems: [],
        questions: [],
        answerChoices: [],
        images: [],
        correctAnswers: [],
        equations: [],
    },
    reducers: {
        addProblemToUpdateQueue: (state, { payload }) => {
            if(!state.problems.some(problem => problem.id === payload.id)) {
                state.problems.push(payload)
            } else {
                state.problems = [...state.problems.filter(problem => problem.id !== payload.id), payload]
            }
        },
        addQuestionToUpdateQueue: (state, { payload }) => {
            const updatedQuestion = { id: payload.id, question_text: payload.value }
            if(!state.questions.some(question => question.id === payload.id)) {
                state.questions.push(updatedQuestion)
            } else {
                state.questions = [
                    ...state.questions.filter(question => question.id !== payload.id), 
                    updatedQuestion
                ]
            }
        },
        addAnswerChoiceToUpdateQueue: (state, { payload }) => {
            const updatedAnswerChoice = { id: payload.id, choice_text: payload.value }
            if(!state.answerChoices.some(answerChoice => answerChoice.id === payload.id)) {
                state.answerChoices.push(updatedAnswerChoice)
            } else {
                state.answerChoices = [
                    ...state.answerChoices.filter(answerChoice => answerChoice.id !== payload.id), 
                    updatedAnswerChoice
                ]
            }
        },
        addImageToUpdateQueue: (state, { payload }) => {
            if(!state.images.some(image => image.id === payload.id)) {
                state.images.push(payload)
            } else {
                state.images = [
                    ...state.images.filter(image => image.id !== payload.id), 
                    payload
                ]
            }
        },
        addCorrectAnswersToUpdateQueue: (state, { payload } ) => {
            if(!state.correctAnswers.some(correctAnswer => correctAnswer.id === payload.id)) {
                state.correctAnswers.push(payload)
            } else {
                state.correctAnswers = [...state.correctAnswers.filter(correctAnswer => correctAnswer.id !== payload.id), payload]
            }
        },
        addEquationToUpdateQueue: (state, { payload }) => {
            console.log('TODO: add equations edditing logic') // @todo
        },
        resetUpdateQueue: (state) => {
            state.problems = [],
            state.questions = [],
            state.answerChoices = [],
            state.images = [],
            state.correctAnswers = []
        }
    }
})


export const { 
    addProblemToUpdateQueue,
    addQuestionToUpdateQueue, 
    addAnswerChoiceToUpdateQueue,
    addImageToUpdateQueue,
    addCorrectAnswersToUpdateQueue,
    resetUpdateQueue
} = updateSlice.actions;

export default updateSlice.reducer;