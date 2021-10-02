import axios from 'axios'

export const fetchProblems = (skripta_id, section_id = null) => {
    let apiUrl = `${window.location.origin}`;

    if(section_id) {
        apiUrl += `/api/skripta/${skripta_id}/${section_id}`
    } else {
        apiUrl += `/api/skripta/${skripta_id}`
    }
    console.log(apiUrl)
    
    return axios.get(apiUrl)
}

export const postProblems = (formData) => {
    let apiUrl = window.location.origin += '/api/question/update';
    
    return axios.post(
        apiUrl,
        formData
    ).then(res => {
        console.log(`Successfully sent form data` + res.data);
     })
    .catch(err => {
        console.log(err);
    })
}