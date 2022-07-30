import React, { useState, useEffect } from "react";

// SHOPIFY
import { TextStyle, Collapsible, TextContainer, Button, Badge, Stack } from "@shopify/polaris";

// REDUX
import { useDispatch, useSelector } from "react-redux";
import { addItem, updateAnswerChoiceText, updateQuestionText, updateSubquestionText } from "../../store/importerSlice";

// UTILS
import { generateProblemObject } from "../../utils/generateProblemObject";

// COMPONENTS
import { EditableTextField } from "../EditableTextField";

// STYLES
import styled from 'styled-components'

const Wrapper = styled.div`
    padding-bottom: 1.6rem;
`


export default function ProblemsTableItem({ id, text, line_data, confidence, confidence_rate, image }) {
  	const dispatch = useDispatch()
	const { items } = useSelector(store => store.importer)

	const [isOpen, setIsOpen] = useState(true);
  	const [problem, setProblem] = useState({
		question: { question_text: 'Lorem ispum dorem cit', confidence: 0, subquestions: [], answer_choices: [] },
		number: '0.'
	});

	useEffect(() => {
		generateProblem()
	}, [line_data])

	useEffect(() => {
		if(problem.number != '0.' && !items.some(item => item.id === problem.id) ) {
			dispatch(addItem(problem))
		}
	}, [problem])
  

	const handleToggle = () => {
		setIsOpen(!isOpen);
	};

  	const generateProblem = () => {
		try {
			const prob = generateProblemObject(text, line_data, image, id)
		  	setProblem(prob);
			dispatch(addItem(prob))
	
			setTimeout(() => {window.MathJax?.typeset()}, 800)
		} catch (error) {	
			console.log(error)
		}
  	}
	
	const badgeStatus = (confidence) => {
		confidence = confidence <= 1 ? Math.round((confidence + Number.EPSILON) * 100) : confidence;
		return confidence >= 80 ? 'success' : confidence < 80 && confidence >= 60 ? 'attention' : confidence < 60 && confidence >= 40 ? 'warning' : 'critical';
	}

	return (
		<>
			<Stack>
				<Stack.Item fill>
					<TextStyle variation="strong">
						{problem.number} Zadatak
					</TextStyle>
				</Stack.Item>
				<Stack.Item>
					<Button onClick={handleToggle} ariaExpanded={isOpen}>
						{isOpen ? 'Close' : 'Open'}
					</Button>
				</Stack.Item>
			</Stack>
			Result quality: <Badge status={badgeStatus(confidence)}>{confidence}%</Badge> | Input quality: <Badge status={badgeStatus(confidence_rate)}>{confidence_rate}%</Badge>
			<Collapsible
				open={isOpen}
				transition={{ duration: "300ms", timingFunction: "ease-in-out" }}
				expandOnPrint
			>	
				<TextContainer>
					<img
						src={image?.image}
						width="100%"
						height="100%"
						style={{
							marginTop: "1.6rem",
							objectFit: "cover",
							objectPosition: "center"
						}}
					/>						
					<EditableTextField 
						key={problem.id}
						id={problem.id}
						value={problem.question.question_text}
						children={<Badge status={badgeStatus(problem.question.confidence)}>Question text</Badge>}
						containsMath
						canContainImages
						onChangeFn={(data) => dispatch(updateQuestionText(data))}
					/>	
					<Stack vertical>
						{problem.question.answer_choices.map( (choice, index) => {
							return(
								<EditableTextField 
									key={index}
									index={index}
									id={problem.id}
									label={`${String.fromCharCode(index+65)}. `}
									value={choice.choice_text}
									children={<Badge status={badgeStatus(choice.confidence)} >Answer choice</Badge>}
									containsMath
									canContainImages
									onChangeFn={(data) => dispatch(updateAnswerChoiceText(data))}
								/>
							)
						})}
					</Stack>
					<Stack vertical>
						{problem.question.subquestions.map( (subquestion, index) => {
							return (
								<EditableTextField 
									key={`sq-${problem.id}`}
									id={problem.id}
									index={index}
									value={subquestion.question_text}
									children={<Badge status={badgeStatus(subquestion.confidence)}>Subuestion text</Badge>}
									containsMath
									canContainImages
									onChangeFn={(data) => dispatch(updateSubquestionText(data))}
								/>	
							)
						})}
					</Stack>
				</TextContainer>
			</Collapsible>
		</>
	)
}
