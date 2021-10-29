// REACT & REDUX
import React, { useState, useCallback, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';

// SHOPIFY
import { TextField } from '@shopify/polaris';

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGripLinesVertical, faPen, faCheckCircle, faTimesCircle } from '@fortawesome/free-solid-svg-icons'

// QRcode
import QRCode from 'qrcode.react'

// COMPONENTS
import ProblemChoice from "./ProblemChoice";
import Subquestions from './Subquestions';
import ProblemImage from "./ProblemImage";

// ACTIONS
import { addQuestion, approveProblem } from "../../store/actions/problemFieldsActions";

const Problem = ({ sectionIndex, problem_index, problem } ) => {
  const [problemId, setProblemId] = useState(problem.id)
  const [problemIndex, setProblemIndex] = useState(problem_index+1)
  const [problemName, setProblemName] = useState(problem.name)
  const [questionId, setQuestionId] = useState(problem.question.id)
  const [questionText, setQuestionText] = useState(problem.question.question_text)
  const [subquestions, setSubquestions] = useState(problem.question.subquestions)
  const [questionChoices, setQuestionChocies] = useState(problem.question.answer_choices)
  const [questionImages, setQuestionImages] = useState(problem.question.images);
  const [approvalStatus, setApprovalStatus] = useState(problem.approval === 'approved' ? true : false);
  const [editFieldOpen, setEditFieldOpen] = useState(false);
  const [hasChanged, setHasChanged] = useState(false)
  const [isFromMatura, setIsFromMatura] = useState(problem.matura)
  const [numberOfChoiceImages, setNumberOfChoiceImages] = useState(problem.question.answer_choices.filter( choice => choice.images.length > 0).length)
  
  const vimeo_embed_src = problem?.video_solution?.vimeo_embed_url ? problem.video_solution.vimeo_embed_url : problem?.video_solution?.vimeo_id ? `https://player.vimeo.com/video/${problem.video_solution.vimeo_id}` : false;

  const qrUrl = problem?.matura && vimeo_embed_src ? `https://gradivo.hr/products/${problem?.matura.subject.subject_name}-matura-${problem?.matura.year.year-1}-${(problem?.matura.year.year).toString(10).slice(-2)}?brZad=${problem?.id}` : false;
  const choiceLabel = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6 : 'G', 7 : 'H' }
  
  const dispatch = useDispatch()
  const view = useSelector( state => state?.problems_view )
  const problem_fields = useSelector(state => state?.problem_fields)

  const mathTypeset = () => {
    if( window.MathJax ) {
      console.log("MathJax typset succesfull")
      window.MathJax.typesetPromise().catch((err) => console.log('Typeset failed: ' + err.message));
    }
  }

  const handleEditFieldToggle = () => {
    if( editFieldOpen && hasChanged) {
      mathTypeset()
    }
    setEditFieldOpen(
      (editFieldOpen) => !editFieldOpen
    ) 
  }

  const handleChange = (newValue, id) => {
    setQuestionText(newValue)
    setHasChanged(true)
    dispatch(addQuestion(newValue, id))
    console.log(problem_fields)
  };
  
  const handleApproveBtn = (approval, id) => {
    approval = approval ? 'approved' : 'unapproved';
    dispatch(approveProblem(approval, id))
    setApprovalStatus(approval)
    console.log(problem_fields)
  }


  const changeProblemTextElement = () => {
    return { __html: 
      `<span>${questionText}</span>`
    };
  }

  const printProblemText = () => {
    if(isFromMatura){
      return { __html: 
        `<strong>${sectionIndex}.${problemIndex}.</strong> <span>(<i>${problemName}</i>) ${questionText.split(' ').splice(1).join(' ')}</span>`
      };
    } else {
      return { __html: 
        `<strong>${sectionIndex}.${problemIndex}.</strong> <span>${questionText}</span>`
      };
    }
  }

  const choiceImageWidthClasses = {
    '1': 'problem__choices--with-images problem__choices--with-images--single',
    '2': 'problem__choices--with-images problem__choices--with-images--half',
    '3': 'problem__choices--with-images problem__choices--with-images--third',
    '4': 'problem__choices--with-images problem__choices--with-images--quarter',
    '5': 'problem__choices--with-images problem__choices--with-images--fifth',
  }

  return (
    <div className="drag-item">
      <div className='problem'>
        {view.editing &&
          <div className="drag-handle">
            <FontAwesomeIcon icon={faGripLinesVertical} />
          </div>
        }
        <div className="problem__content-container">
          <div className="problem__content">
            {view.site_preview && vimeo_embed_src && 
              <div className="problem__video">
                <iframe src={vimeo_embed_src} 
                        frameBorder="0" 
                        allow="autoplay; fullscreen; picture-in-picture" 
                        allowFullScreen 
                        title="26">
                </iframe>
                <script src="https://player.vimeo.com/api/player.js"></script>
              </div>
            }
            {!view.printing && <div className="problem__text" dangerouslySetInnerHTML={changeProblemTextElement()}></div>}
            {view.printing && <div className="problem__text" dangerouslySetInnerHTML={printProblemText()}></div>}
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
                id={questionId}
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
            {subquestions && subquestions.map( (subquestion, subquestion_index) => {
                return (
                  <Subquestions question={subquestion} subquestion_index={subquestion_index} is_from_matura={isFromMatura} key={subquestion.id}></Subquestions>
                )
              }
            )}
            <div className={`problem__choices ${numberOfChoiceImages > 0 ? choiceImageWidthClasses[numberOfChoiceImages] : ''}`}>
              {questionChoices.map( (choice, index) => {
                return (
                  <ProblemChoice 
                    key={choice.id} 
                    choice={choice} 
                    choice_label={`${choiceLabel[index]}.`}
                    problem={problem}
                  />
                  )
                })}
            </div>
          </div>
        </div>
        {!view.editing && !view.site_preview && qrUrl && <a className="problem__qr-link" href={qrUrl}><QRCode value={qrUrl} renderAs="svg" /></a>}
      </div>
      {view.site_preview && 
        <div className="problem__footer">
          <div className={`problem__approval-status ${approvalStatus ? 'problem__approval-status--approved' : 'problem__approval-status--unapproved'}`}>
            {approvalStatus ? 'Approved' : 'Not approved'}
          </div>
          <div className="problem__btns">
            <div className="problem__unapprove">
              <button className='btn btn--primary' onClick={() => handleApproveBtn(false, problemId)} ><FontAwesomeIcon icon={faTimesCircle} /></button>
            </div>
            <div className="problem__approve">
              <button className='btn btn--save' onClick={() => handleApproveBtn(true, problemId)} ><FontAwesomeIcon icon={faCheckCircle} /></button>
            </div>
          </div>
        </div>
      }
  </div>
  )
}

export default Problem;