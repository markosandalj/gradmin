import React from 'react'
import { useParams } from 'react-router';

// COMPONENTS
import { TextStyle, Stack } from '@shopify/polaris';

// STYLES
import styled from 'styled-components'

// COMPONENTS
import { ProblemImage } from './parts/ProblemImage'
import { EditableTextField } from './EditableTextField';

// REDUX
import { useDispatch } from 'react-redux';
import { addAnswerChoiceToUpdateQueue, addCorrectAnswersToUpdateQueue } from '../store/updateSlice';


const Table = styled.div`
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    border-top: 1px solid gray;
    border-left: 1px solid gray;
`

const TableItem = styled.div`
    flex: .25;
    display: flex;
    padding: .5rem;
    border-bottom: 1px solid gray;
    border-right: 1px solid gray;
`

export const SolutionsTable = ({ section, sectionNumber }) => {

    const dispatch = useDispatch()

    const { section_order } = useParams();
    
    if(!section) return <></>;

    return (
        <Table>
            {section.problems?.map((problem, index) => {
                return (
                    <TableItem key={`solutionTableItem-${problem.id}`}>
                        {problem.question.correct_answer.map(correctAnswer => {
                            return(
                                <div key={`correctAnswer-${correctAnswer.id}`}>
                                    <Stack vertical>
                                        <Stack.Item>
                                            <TextStyle variation="strong">
                                                {section_order ? section_order : sectionNumber}.{index+1}.
                                            </TextStyle>
                                        </Stack.Item>
                                        <Stack.Item>
                                            <EditableTextField 
                                                value={correctAnswer.answer_choice?.choice_text}
                                                id={correctAnswer.answer_choice?.id}  
                                                containsMath
                                                onChangeFn={() => dispatch(addAnswerChoiceToUpdateQueue)}
                                            />
                                        </Stack.Item>
                                        {correctAnswer.answer_choice?.images.map(image => {
                                            return (
                                                <Stack.Item>
                                                    <ProblemImage image={image} key={`solutionChoiceImage-${image.id}`} />
                                                </Stack.Item>
                                            )
                                        })}
                                        <Stack.Item>
                                            <EditableTextField 
                                                value={correctAnswer.answer_text}
                                                id={correctAnswer.id}  
                                                containsMath
                                                onChangeFn={() => dispatch(addCorrectAnswersToUpdateQueue)}
                                            />
                                        </Stack.Item>
                                            {correctAnswer.images.map(image => {
                                                return (
                                                    <Stack.Item>
                                                        <ProblemImage key={`solutionImage-${image.id}`} image={image} />
                                                    </Stack.Item>
                                                )
                                            })}
                                    </Stack>
                                </div>
                            )
                        })}
                    </TableItem>
                )
            })}
        </Table>
    )
}
