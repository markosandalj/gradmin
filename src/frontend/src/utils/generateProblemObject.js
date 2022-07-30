export const generateProblemObject = (text, line_data, image, id) => {
    const problemNumberInteger = parseInt(text?.split(' ')[0], 10)
    const problemNumberString = Number.isInteger(problemNumberInteger) ? text?.split(' ')[0].replace(/\s/g, '') : null;

    return {
        id: id,
        number: problemNumberString,
        question: constructQuestionObject(line_data, problemNumberInteger),
        image_id: image.id,
        image_public_id: image.image.replace('https://res.cloudinary.com/gradivo-hr/image/upload/', ''),
    }
}


const isAnswerChoice = (text) => {
    let hasLabel = false

    for(let i = 65; i <= 78; i++ ) {
        if(text.startsWith(`${String.fromCharCode(i)}.`) || text.startsWith(`\n${String.fromCharCode(i)}.`)) {
            hasLabel = true
            break
        }
    }
    
    return text && hasLabel
}


const constructQuestionObject = (line_data, problemNumberInteger) => {
    let question = {}
    let subquestions = []
    let answer_choices = []
    let question_text = ''
    let question_confidence = 0
    let subquestion_text = ''
    let subquestion_confidence = 0
    let answer_choice_text = ''
    let answer_choice_confidence = 0
    
    let subquestion_line_index = 0
    let question_line_index = 0
    let answer_choice_line_index = 0
    let index = 1

    line_data.forEach((line, i) => {
        if(line.type !== 'text' || !line.included) return;

        if(!isSubquestion(line, index, problemNumberInteger) && !isAnswerChoice(line.text)) {
            if(!subquestion_text.length && !answer_choice_text.length) {
                question_text += line.text
                question_confidence = (question_line_index * question_confidence + line.confidence)/(question_line_index + 1)
                question_line_index++;
            }
            if(subquestion_text.length) {
                subquestion_text += line.text
                subquestion_confidence = (subquestion_line_index * subquestion_confidence + line.confidence)/(subquestion_line_index + 1)
                subquestion_line_index++;
            }
            if(answer_choice_text.length) {
                answer_choice_text += line.text
                answer_choice_confidence = (answer_choice_line_index * answer_choice_confidence + line.confidence)/(answer_choice_line_index + 1)
                answer_choice_line_index++;
            }
        } else {
            if(answer_choice_text.length) {
                answer_choices.push({ choice_text: formatAnswerChoice(answer_choice_text), confidence: answer_choice_confidence, images: [] })
                answer_choice_text = ''
                answer_choice_confidence = 0
                answer_choice_line_index = 0
            }
        
            if(question_text.length) {
                question = { question_text: question_text, confidence: question_confidence }
                question_text = ''
                question_confidence = 0
                question_line_index = 0
            }
        
            if(subquestion_text.length) {
                subquestions.push({ question_text: subquestion_text, confidence: subquestion_confidence })
                subquestion_text = ''
                subquestion_confidence = 0
                subquestion_line_index = 0
            }
        }

        if(isSubquestion(line, index, problemNumberInteger)) {
            index++
            subquestion_text = line.text
            subquestion_confidence = (subquestion_line_index * subquestion_confidence + line.confidence)/(subquestion_line_index + 1)
            subquestion_line_index++;
        }

        if(isAnswerChoice(line.text)) {
            answer_choice_text = line.text
            answer_choice_confidence = (answer_choice_line_index * answer_choice_confidence + line.confidence)/(answer_choice_line_index + 1)
            answer_choice_line_index++;
        }
    })

    if(answer_choice_text.length) {
        answer_choices.push({ choice_text: formatAnswerChoice(answer_choice_text), confidence: answer_choice_confidence, images: [] })
    }

    if(question_text.length) {
        question = { question_text: question_text, confidence: question_confidence }
    }

    if(subquestion_text.length) {
        subquestions.push({ question_text: subquestion_text, confidence: subquestion_confidence })
    }

    return {
        ...question,
        subquestions: subquestions,
        answer_choices: answer_choices
    };
}

const formatAnswerChoice = (text) => {
    return text.length <= 4 ? '(slika)' : text.substr(4, text.length)
}


const isSubquestion = (line, index, problemNumberInteger) => {
    let firstWord = line.text.split(' ')[0]

    if(!firstWord.match(/(\d.\d.)/g)) return false;

    let firstNumber = parseInt(firstWord.split('.')[0], 10)
    let secondNumber = parseInt(firstWord.split('.')[1], 10)

    if(firstNumber !== problemNumberInteger) return false;

    if(secondNumber !== index) return false;

    return true
}

const reducedExample = {
    number: '1.',
    question: {
        question_text: '',
        subquestions: [],
        correct_answers: [],
        answer_choices: [{
            choice_text: '',
            images: [{
                image: '',
                image_dark: ''
            }]
        }],
        images: [{
            image: '',
            image_dark: ''
        }], 
    },
}

// problem
const example = {
    id: 1, // won't use, calculated on BE
    name: 'Ime zadatka', // won't use, calculated on BE
    number: '1.',
    approval: '', // won't use, has defaults
    shop_availability: '', // won't use, , has defaults
    question: {
        id: 1, // won't use, calculated on BE
        question_text: '',
        subquestions: [],
        correct_answers: [],
        answer_choices: [{
            id: 1, // won't use, calculated on BE
            choice_text: '',
            images: []
        }],
        images: [{
            id: 1,
            image: "",
            image_dark: ''
        }],    
    },
    video_solution: null, // won't use
    section: null, // might use but not prio
    matura: null, // won't use, calculated on BE
    skripta: null, // won't use, calculated on BE
    subject: null // won't use, calculated on BE
}