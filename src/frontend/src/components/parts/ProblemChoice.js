// REACT
import React, { useCallback } from "react";

// REDUX
import { useSelector, useDispatch } from 'react-redux';
import { addAnswerChoiceToUpdateQueue } from '../../store/updateSlice';

// SHOPIFY
import { Badge } from "@shopify/polaris";

// COMPONENTS
import { EditableTextField } from "../EditableTextField";

// SETTINGS
import { REVIEW_VIEW_TYPE, SUCCESS } from "../../settings/constants";

export const ProblemChoice = ({ choice, isCorrect, label }) => {
    const dispatch = useDispatch()
    const viewType = useSelector(store => store.view.viewType)
    
    if(!choice) return <></>

    return (
        <>
            <EditableTextField
                value={choice.choice_text}
                children={isCorrect && viewType === REVIEW_VIEW_TYPE ? <Badge size="small" status={SUCCESS}>Točan odgovor</Badge> : null}
                id={choice.id}
                containsMath
                onChangeFn={() => dispatch(addAnswerChoiceToUpdateQueue)}
                label={label}
            />
        </>
    )
}