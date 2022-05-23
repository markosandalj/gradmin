// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { ResourceItem, TextStyle, Collapsible, TextContainer, Button, Badge, ButtonGroup } from "@shopify/polaris";

export default function ProblemsTableItem({ id, text, line_data, confidence, confidence_rate, image, formData, setFormData }) {
  const [isOpen, setIsOpen] = useState(true);
  const [problem, setProblem] = useState({
		question: { text: 'Lorem ispum dorem cit', confidence: 0 },
		answer_choices: [],
		number: '0.'
	});

  useEffect(() => {
	generateProblem()
  }, [line_data])

  useEffect(() => {
	if(problem.number != '0.') {
		formData.problems.push(problem)
		setFormData({
			...formData
		})
	}
  }, [problem])
  

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  const choiceLabel = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6 : 'G', 7 : 'H' }

  	const generateProblem = () => {
		let problem_text = text;
		let problem_number = ''
		let question = { text: '', confidence: 0 }
		let answer_choices = []

		try {
			const isAnswerChoice = (text) => {
				return ( text ? (text?.startsWith('\nA.') 
						|| text?.startsWith('\nB.') 
						|| text?.startsWith('\nC.') 
						|| text?.startsWith('\nD.') 
						|| text?.startsWith('\nE.')) : false
					)
			}
			
			line_data.map((item, index) => {
				question.text += (item.included && !isAnswerChoice(item.text)) ? item.text : '';
				question.confidence = (item.included && !isAnswerChoice(item.text)) ? (index * question.confidence + item.confidence)/(index + 1) : question.confidence;
				
				if(isAnswerChoice(item.text)) {
					answer_choices.push({
						text: item.text,
						confidence: item.confidence
					})
				}
			})
	
			problem_number = Number.isInteger(parseInt(text?.split(' ')[0], 10)) ? text?.split(' ')[0].replace(/\s/g, '') : null
	
			answer_choices = answer_choices.map( item => {
				return {
					...item,
					text: item?.text.length <= 4 ? '(slika)' : item?.text.substr(4, item?.text.length)
				}
			})
	
			setProblem({
				id: id,
				image_public_id: image.image.replace('https://res.cloudinary.com/gradivo-hr/image/upload/', ''),
				image_id: image.id,
				question: question,
				answer_choices: answer_choices,
				number: problem_number
			});
	
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
			<div>
				<div className="flex-space-between">
					<h3>
						<TextStyle variation="strong">
							{problem.number} Zadatak
						</TextStyle>
					</h3>
					<Button onClick={handleToggle} ariaExpanded={isOpen}>
						{isOpen ? 'Close' : 'Open'}
					</Button>
				</div>
				<div>
					Result quality: <Badge status={badgeStatus(confidence)}>{confidence}%</Badge> | Input quality: <Badge status={badgeStatus(confidence_rate)}>{confidence_rate}%</Badge>
				</div>
			</div>
			<Collapsible
				open={isOpen}
				id="basic-collapsible"
				transition={{ duration: "300ms", timingFunction: "ease-in-out" }}
				expandOnPrint
			>	
				<div className="my-1">
					<TextContainer>
						<img
							src={image?.image}
							alt=""
							width="100%"
							height="100%"
							style={{
								objectFit: "cover",
								objectPosition: "center"
							}}
						/>
						
						<div className="problem__content">
							<div className="flex-space-between">
								<span>{problem.question.text}</span> <Badge status={badgeStatus(problem.question.confidence)}>Question text</Badge>
							</div>
							<div className="problem__choices">
								{problem.answer_choices.map( (choice, index) => {
									return(
										<div key={index} className="flex-space-between">
											<div  className='problem__choice'>{choiceLabel[index]}. {choice.text}</div>
											<Badge status={badgeStatus(choice.confidence)} >Answer choice</Badge>
										</div>
									)
								})}
							</div>
						</div>
				</TextContainer>
				</div>
			</Collapsible>
		</>
	);
	}
