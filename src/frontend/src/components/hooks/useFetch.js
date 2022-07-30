import React, { useEffect, useState } from 'react';
import axios from 'axios'

// REDUX
import { useDispatch } from 'react-redux'
import { toggleLoading } from '../../store/pageSlice';


const useFetch = (apiUrl) => {
    const dispatch = useDispatch()
    const [data, setData] = useState(null); 
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(null);
    
    useEffect(() => { 
        console.log('Fetching from: ', apiUrl)
        dispatch(toggleLoading())
        axios(apiUrl) 
            .then((response) => { 
                setData(response.data); 
            }) 
            .catch((error) => { 
                console.error("Error fetching data: ", error); 
                setError(error); 
            }) 
            .finally(() => { 
                setLoading(false); 
                dispatch(toggleLoading())
                console.log("Fetching done"); 
            });
    }, []);

    return {data, loading, error}
}

export default useFetch;