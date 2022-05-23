// REACT & REDUX
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";


import ApiRoutes from "../config/ApiRoutes";

const handlePrint = async( selector, pdfFileName = 'tmp', id = null, cssFileName = 'print') => {
        const apiUrl = ApiRoutes.print
        const printElement = document.querySelector(selector)

        // TO-DO implement namings on BE 11.05.2022
        let formData = new FormData();
        formData.append('html', JSON.stringify(printElement.innerHTML) ) 
        formData.append('css_file', cssFileName)
        formData.append('pdf_name', pdfFileName)
        formData.append('id', id)

        
        return await axios.post(apiUrl, formData, {
                    headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"}}
                )
                .then((response) => { 
                    console.log(`Response from ${apiUrl}: `, JSON.parse(response.data))
                    return JSON.parse(response.data)
                }) 
                .catch((error) => { 
                    console.error("Error fetching data: ", error); 
                    return error
                })
}

export default handlePrint;