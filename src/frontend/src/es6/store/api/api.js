import axios from 'axios'
import ApiRoutes from '../../components/config/ApiRoutes';

export const fetchCheatsheet = (id) => {
    let apiUrl = ApiRoutes.cheatsheets + id;
    
    return axios.get(apiUrl)
}

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

export const fetchMaturaList = (subject_id) => {
    let apiUrl = `${window.location.origin}/${subject_id}/list`;

    return axios.get(apiUrl)
}

export const fetchMaturaProblems = (matura_id) => {
    let apiUrl = `${window.location.origin}/${matura_id}`;

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