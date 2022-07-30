import { createSlice, current } from "@reduxjs/toolkit";
import { SORT_CONFIDENCE_HIGHEST, SORT_CONFIDENCE_LOWEST, SORT_PROBLEMS_NUMBER_DESC } from "../settings/constants";

export const importerSlice = createSlice({
    name: "importer",
    initialState: {
        file: null,
        isUploadInProgress: false,
        isUploadDone: false,
        selectedMatura: null,
        selectedSubject: null,
        selectedSkritpa: null,
        selectedSection: null,
        items: []
    },
    reducers: {
        setSelectedMatura: (state, { payload }) => {
            state.selectedMatura = payload
        },
        setSelectedSubject: (state, { payload }) => {
            state.selectedSubject = payload
        },
        setSelectedSkripta: (state, { payload }) => {
            state.selectedSkritpa = payload
        },
        setSelectedSection: (state, { payload }) => {
            state.selectedSection = payload
        },
        setFile: (state, { payload }) => {
            state.file = payload
        },
        resetImporter: (state) => {
            state.file = null
            state.isUploadInProgress = false
            state.isUploadDone = false
            state.selectedMatura = null
            state.selectedSubject = null
            state.selectedSkritpa = null
            state.selectedSection = null
            state.items = []
        },
        setUploadInProgress: (state) => {
            state.isUploadDone = false
            state.isUploadInProgress = true
        },
        setUploadIsDone: (state) => {
            state.isUploadInProgress = false
            state.isUploadDone = true
        },
        addItem: (state, { payload }) => {
            let item = { ...current(state.items).find(item => item.id === payload.id), ...payload }
            state.items = [...current(state.items).filter(item => item.id !== payload.id), item]
        }, 
        setItems: (state, { payload }) => {
            state.items = payload
        },
        sortItems: (state, { payload }) => {
            switch (payload) {
                case SORT_CONFIDENCE_HIGHEST:
                    state.items = current(state.items).sort((a, b) => b.mathpix_response.confidence - a.mathpix_response.confidence)
                    break;
                case SORT_CONFIDENCE_LOWEST:
                    state.items = current(state.items).sort((a, b) => a.mathpix_response.confidence - b.mathpix_response.confidence)
                    break;
                case SORT_PROBLEMS_NUMBER_DESC:
                    state.items = current(state.items)
                    break;
                default:
                    break;
            }
        },
        updateQuestionText: (state, { payload }) => {
            const { id, value } = payload
            let itemIndex = 0
            let item = {...current(state.items).find((item, index) => {
                itemIndex = index
                return item.id === id
            })}
            item.question = { ...item.question, question_text: value }

            state.items = [...current(state.items)].map((itm, index) => index === itemIndex ? item : itm)
        },
        updateSubquestionText: (state, { payload }) => {
            const { id, value, index } = payload
            let itemIndex = 0
            let item = {...current(state.items).find((item, index) => {
                itemIndex = index
                return item.id === id
            })}

            let subquestions = [...item.question.subquestions].map((subq, i) => 
                i === index ? 
                    { ...item.question.subquestions[index], question_text: value } : subq
            )
            
            item.question = {...item.question, subquestions: subquestions }

            state.items = [...current(state.items)].map((itm, index) => index === itemIndex ? item : itm)
        },
        updateAnswerChoiceText: (state, { payload }) => {
            const { id, value, index } = payload
            let itemIndex = 0
            let item = {...current(state.items).find((item, index) => {
                itemIndex = index
                return item.id === id
            })}

            let answerChoices = [...item.question.answer_choices].map((ans_choice, i) => 
                i === index ? 
                    { ...item.question.answer_choices[index], choice_text: value } : ans_choice
            )

            item.question = {...item.question, answer_choices: answerChoices }

            state.items = [...current(state.items)].map((itm, index) => index === itemIndex ? item : itm)
        }
    }
})


export const {
    setSelectedMatura,
    setSelectedSubject,
    setSelectedSkripta,
    setSelectedSection,
    setFile,
    resetImporter,
    setUploadInProgress,
    setUploadIsDone,
    addItem,
    setItems,
    sortItems,
    updateQuestionText,
    updateAnswerChoiceText,
    updateSubquestionText
} = importerSlice.actions;

export default importerSlice.reducer;