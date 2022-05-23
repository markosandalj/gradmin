import axios from 'axios'
import { useEffect, useState } from 'react';

const useFetch = (apiUrl, dependencyArray = [] ) => {
    const [data, setData] = useState(null); 
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(null);

    useEffect(() => { 
        const fetchData = async () => {
            console.log('Fetching: ', apiUrl)        
            setLoading(true)
            await axios(apiUrl) 
                .then((response) => { 
                    console.log(`Response from ${apiUrl}: `, response.data)
                    setData(response.data); 
                }) 
                .catch((error) => { 
                    console.error("Error fetching data: ", error); 
                    setError(error); 
                }) 
                .finally(() => { 
                    setLoading(false); 
                });
        }

        if(apiUrl) fetchData();

    }, dependencyArray);

    return {data, loading, error}
}

export default useFetch;