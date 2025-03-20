import axios from 'axios';
import React, { useEffect, useState } from 'react'

export default function Home() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/users/api/')
        .then((res) => {
            setData(res.data);
            setLoading(false);
        })
        .catch((err) => {
            setError(err);
            setLoading(false);
        });
    }, []);

    if (loading) {return <div>Loading...</div>;}

    if (error) {return <div>Error: {error.message}</div>}



  return (
    <div>
        <h1>Datos de la API desde Django</h1>
        <ul>
            {data.map((item)=>(
                <li key={item.id}>{JSON.stringify.item}</li>

            ))}
        </ul>
        
    </div>
  )
}
