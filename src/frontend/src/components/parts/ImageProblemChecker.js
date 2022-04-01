// REACT & REDUX
import React, { Component, useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

// SHOPIFY
import { Page, Layout, Button, Spinner, Banner, MediaCard, ButtonGroup } from '@shopify/polaris';


export default function ImageProblemsChecker({mathpixResposneData, activeImage, setActiveImage, formData, setFormData}) {
    const [problem, setProblem] = useState({
        question_text: 'Lorem ispum dorem cit',
        answer_choices: [],
        number: '0.'
    });

    
    const choiceLabel = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6 : 'G', 7 : 'H' }
    
    const nextImage = () => {
        let index = mathpixResposneData.findIndex(item => item.image.id === activeImage.image.id)
        let next = mathpixResposneData[index + 1]
        setActiveImage(next)
    }

    const prevImage = () => {
        let index = mathpixResposneData.findIndex(item => item.image.id === activeImage.image.id)
        let prev = mathpixResposneData[index - 1]
        setActiveImage(prev)
    }

    const hasNextImage = () => {
        let index = mathpixResposneData.findIndex(item => item.image.id === activeImage.image.id)
        let next = mathpixResposneData[index + 1]
        
        return next ? true : false;
    }

    const hasPrevImage = () => {
        let index = mathpixResposneData.findIndex(item => item.image.id === activeImage.image.id)
        let prev = mathpixResposneData[index - 1]
        
        return prev ? true : false;
    }

    const isAnswerChoice = (text) => {
        return (text.startsWith('\nA.') 
                || text.startsWith('\nB.') 
                || text.startsWith('\nC.') 
                || text.startsWith('\nD.') 
                || text.startsWith('\nE.')
            )
    }

    const generateProblem = () => {
        let text = activeImage?.mathpix_response.text;
        let problem_number = ''
        let question_text = ''
        let answer_choices = []
        
        activeImage?.mathpix_response?.line_data.map((item, index) => {
            question_text += (item.included && !isAnswerChoice(item.text)) ? item.text : ''
            if(isAnswerChoice(item.text)) answer_choices.push(item.text)
        })

        problem_number = Number.isInteger(parseInt(text.substr(0, 2), 10)) ? text.substr(0,2).replace(/\s/g, '') : null
        answer_choices = answer_choices.map( item => {
            return item.length <= 5 ? '(slika)' : item.substr(4, item.length)
        })

        setProblem({
            question_text: question_text,
            answer_choices: answer_choices,
            number: problem_number
        });

        setTimeout(() => {window.MathJax?.typeset()}, 800)
    }

    const problemElement = () => {
        return { __html: `
            ${problem.question_text}
            <div className="problem__choices">
                ${problem.answer_choices?.map( (choice, index) => {
                    return (`<div key=${index} className='problem__choice'>${choiceLabel[index]}. ${choice}</div>`)
                })}
            </div>`}
    }

    const addProblemData = () => {
        let prob = {
            index: mathpixResposneData.findIndex(item => item.image.id === activeImage.id),
            matura: formData?.matura,
            subject: formData?.subject,
            section: formData?.section,
            skripta: formData?.skripta,
            name: formData?.matura?.label + problem?.number,
            number: problem?.number,
            question: {
                question_text: problem.question_text,
                answer_choices: problem.answer_choices,
                subquestions: [],
                correct_answers: []
            },
        }

        setFormData({
            ...formData,
            problems: {
                [prob[prob.index]]: prob,
            }
        })
    }

    const submitFormData = () => {

        let data = new FormData();

        data.append('data', JSON.stringify(formData))

        console.log(window.location.origin + '/api/problems_importer/update')

        axios.post(
                window.location.origin + '/api/problems_importer/update',
                data,
                { headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"} }
            )
            .then(res => res.data)
            .catch(err => console.log(err))
    }

    useEffect( () => {
        if(activeImage) generateProblem();
    }, [activeImage])

    useEffect( () => {
        if(problem && window.MathJax) setTimeout(() => {window.MathJax?.typeset()}, 600);
    }, [problem])


    return (
        <MediaCard
            size="medium"
            portrait={true}
        >
            <img src={activeImage.image.image} alt="" width="100%" height="100%" 
                style={{
                    objectFit: 'cover',
                    objectPosition: 'center',
                }}
            />
            <div className="problem--importer">
                <div className="problem__content" dangerouslySetInnerHTML={problemElement()}>
                </div>
                <div className="py-2">
                    <ButtonGroup fullWidth={true} spacing="loose">
                        <Button onClick={prevImage} disabled={!hasPrevImage()}>Prošli</Button>
                        <Button onClick={nextImage} disabled={!hasNextImage()}>Sljeceći</Button>
                    </ButtonGroup>
                </div>
                <div className="py-2">
                    <ButtonGroup fullWidth={true} spacing="loose">
                        <Button primary onClick={addProblemData}>Zadatak je dobar</Button>
                        <Button primary outline onClick={submitFormData}>Završi</Button>
                    </ButtonGroup>
                </div>
            </div>
        </MediaCard>
    )
}