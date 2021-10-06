// REACT & REDUX
import React, { useState, useCallback, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';

// SHOPIFY
import { TextField, DropZone } from '@shopify/polaris';

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPen} from '@fortawesome/free-solid-svg-icons'

// ACTIONS
import { addAnswerChoice } from "../../store/actions/problemFieldsActions";

const ProblemChoice = ({ choice, choice_label, problem }) => {
    const [choiceText, setChoiceText] = useState(choice.choice_text)
    const [editChoiceFieldOpen, setEditChoiceFieldOpen] = useState(false);
    const [hasChanged, setHasChanged] = useState(false)
    const [hasImage, setHasImage] = useState( (choice.images).length > 0 || choice.choice_text === '(slika)')
    const [imageSrc, setImgSrc] = useState((choice.images).length > 0 ? choice.images[0].image : null)
    const [file, setFile] = useState();
    const view = useSelector( state => state?.problems_view )
    const answer_choices = useSelector( state => state?.problem_fields )
    const dispatch = useDispatch()

    const handleDropZoneDrop = useCallback(
        (_dropFiles, acceptedFiles, _rejectedFiles) =>
          setFile((file) => acceptedFiles[0]),  
        [],
      );

    const validImageTypes = ['image/gif', 'image/jpeg', 'image/png'];
        
    const fileUpload = !file && <DropZone.FileUpload />;

    const mathTypeset = () => {
        if( window.MathJax ) {
            console.log("MathJax typset succesfull")
            window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
        }
    }

    const handleChange = (newValue, id) => {
        setChoiceText(newValue)
        setHasChanged(true)
        dispatch(addAnswerChoice(newValue, id))
    }

    const handleEditChoiceFieldToggle = () => {
        if(editChoiceFieldOpen && hasChanged) {
            mathTypeset()
        }
        setEditChoiceFieldOpen(
            (editChoiceFieldOpen) => !editChoiceFieldOpen
        ) 
    }

    const changeChoiceTextElement = () => {
        return { __html: `${choice_label} ${choiceText}` };
    }
    
    return (
        <div className='problem__choice'>
            {(choice.images).length > 0}
            {!hasImage && !view.site_preview && <div className="choice__text" dangerouslySetInnerHTML={changeChoiceTextElement()}></div>}
            {hasImage && !view.site_preview && <img className='choice__image' src={imageSrc} /> }
            {view.site_preview && 
                <div className={`choice__input ${problem.question?.correct_answer[0]?.answer_choice?.id === choice.id && 'choice__input--correct' }`}>
                    <input id={choice.id} type="radio" className="choice__checkbox" name={`problem-choices-${problem.question.id}`} />
                    <label htmlFor={choice.id} >
                        {choice_label} {choiceText}
                    </label>
                </div>
            }
            {view.editing && 
                <button type="button" className={ `choice__text-edit ${editChoiceFieldOpen ? 'open' : ''}`} onClick={handleEditChoiceFieldToggle}>
                    <FontAwesomeIcon icon={faPen} />
                </button>
            }
            {editChoiceFieldOpen && view.editing && !hasImage &&
                <TextField
                    value={choiceText}
                    onChange={handleChange}
                    readOnly={false}
                    multiline={4}
                    id={choice.id}
                />}
            {editChoiceFieldOpen && view.editing && hasImage && 
                <DropZone accept="image/*" type="image" allowMultiple={false} onDrop={handleDropZoneDrop}>
                    {fileUpload}
                    {file && file.name}
                </DropZone>
            }
        </div>
    )
}


export default ProblemChoice;