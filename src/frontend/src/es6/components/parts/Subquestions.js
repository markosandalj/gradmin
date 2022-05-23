// REACT & REDUX
import React, { useState, useCallback, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';


// SHOPIFY
import { TextField } from '@shopify/polaris';

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPen } from '@fortawesome/free-solid-svg-icons'

// ACTIONS
import { addQuestion } from "../../store/actions/problemFieldsActions";

// COMPONENTS
import ProblemImage from "./ProblemImage";

const Subquestions = ({question, subquestion_index, is_from_matura}) => {
    const [questionText, setQuestionText] = useState(question.question_text)
    const [subquestions, setSubquestions] = useState(question.subquestions)
    const [questionChoices, setQuestionChocies] = useState(question.answer_choices)
    const [questionImages, setQuestionImages] = useState(question.images);
    const [editFieldOpen, setEditFieldOpen] = useState(false);
    const [hasChanged, setHasChanged] = useState(false)
    const [numberOfChoiceImages, setNumberOfChoiceImages] = useState(question.answer_choices.filter( choice => choice.images.length > 0).length)
    const dispatch = useDispatch()
    const view = useSelector( state => state?.page_view )
    const problem_fields = useSelector(state => state?.problem_fields)
    const choiceLabel = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6 : 'G', 7 : 'H' }
    const subquestionLabel = { 0: 'a)', 1: 'b)', 2: 'c)', 3: 'd)', 4: 'e)', 5: 'f)', 6 : 'g)', 7 : 'h)' }

    const mathTypeset = () => {
      if( window.MathJax ) {
        console.log("MathJax typset succesfull")
        window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
      }
    }
    
    const handleChange = (newValue, id) => {
      setQuestionText(newValue)
      setHasChanged(true)
      dispatch(addQuestion(newValue, id))
      console.log(problem_fields)
    };

    const handleEditFieldToggle = () => {
      if( editFieldOpen && hasChanged) {
        mathTypeset()
      }
      setEditFieldOpen(
        (editFieldOpen) => !editFieldOpen
      ) 
    }

    const imageWidthClasses = {
        '1': 'problem__choices--with-images problem__choices--with-images--single',
        '2': 'problem__choices--with-images problem__choices--with-images--half',
        '3': 'problem__choices--with-images problem__choices--with-images--third',
        '4': 'problem__choices--with-images problem__choices--with-images--quarter',
        '5': 'problem__choices--with-images problem__choices--with-images--fifth',
    }

    return (
        <div className="problem__subquestion">
            <div className="problem__text">{!is_from_matura && subquestionLabel[subquestion_index]} {questionText}</div>
            {view.editing &&
                <button type="button" className={`problem__text-edit ${editFieldOpen && 'open'}`} onClick={handleEditFieldToggle}>
                    <FontAwesomeIcon icon={faPen} />
                </button>
            }
            {editFieldOpen && view.editing &&
                <TextField
                    value={questionText}
                    onChange={handleChange}
                    readOnly={false}
                    multiline={4}
                    id={question.id}
                />
            }
            {questionImages.length > 0 && !view.site_preview &&
              <div className="problem__images">
                {questionImages.map(image => {
                  return (
                    <ProblemImage image={image} key={image.id}></ProblemImage>
                  )
              })}
              </div>
            }
            <div className={`problem__choices ${numberOfChoiceImages > 0 ? imageWidthClasses[numberOfChoiceImages] : ''}`}>
              {questionChoices && questionChoices.map( (choice, index) => {
                return (
                  <ProblemChoice 
                    key={choice.id} 
                    choice={choice} 
                    choice_label={`${choiceLabel[index]}.`}
                  />
                  )
                })}
            </div>
            {subquestions && subquestions.map( (subquestion, index) => {
                return (
                  <Subquestions question={subquestion} key={subquestion.id}></Subquestions>
                )
              }
            )}
        </div>
    )
}

export default Subquestions;