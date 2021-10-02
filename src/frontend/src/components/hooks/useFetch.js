import axios from 'axios'
import { useEffect, useState } from 'react';

const useFetch = (apiUrl) => {
    const [data, setData] = useState(null); 
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(null);

    useEffect(() => { 
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
        });
    }, []);

    return {data, loading, error}
}

export default useFetch;