import React from 'react'

// SHOPIFY
import { Stack } from '@shopify/polaris';

// REDUX
import { useSelector, useDispatch } from 'react-redux';
import { addQuestionToUpdateQueue } from '../../store/updateSlice';

// COMPONENTS
import { ProblemChoice } from './ProblemChoice';
import { ProblemImage} from "./ProblemImage";
import { EditableTextField } from "../EditableTextField";



export const Question = ({ question }) => {
	const dispatch = useDispatch()

	if(!question) return <></>;

    return (	
		<Stack vertical>
			<Stack.Item>
				<EditableTextField
					value={question.question_text}
					id={question.id}
					onChangeFn={() => dispatch(addQuestionToUpdateQueue)}
					containsMath
				/>
			</Stack.Item>
			<Stack.Item>
				{question.images.map(image => {
					return <ProblemImage image={image} key={image.id} />;
				})}
			</Stack.Item>
			<Stack.Item>
				{question.subquestions?.map((subquestion) => {
					return <Question question={subquestion} key={subquestion.id} />
				})}
			</Stack.Item>
			<Stack.Item>
				{question.answer_choices.map((choice, i) => {
					return (
						<ProblemChoice
							key={choice.id} 
							choice={choice} 
							label={`${String.fromCharCode(i+65)}. `}
							isCorrect={question.correct_answer[0]?.answer_choice.id === choice.id}
						/>
					)
				})}
			</Stack.Item>
		</Stack>
    )
}


