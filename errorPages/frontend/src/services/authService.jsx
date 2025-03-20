import axios from "axios";

const API_URL = "http://127.0.0.1:8000/users/token/"

export const login = async(email, password) => {
    const response = await axios.post(API_URL, {email, password});
    if(response.data.access){
        localStorage.setItem("accessToken", JSON.stringify(response.data.access));
        localStorage.setItem("refreshToken", JSON.stringify(response.data.refresh));
    }
    return response.data;
}

export const logout=()=>{
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
}

// To do
// Crear un metodo que jale informacion del usuario para fines de react