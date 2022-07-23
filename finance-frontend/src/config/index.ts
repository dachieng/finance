import { AxiosRequestConfig } from "axios";

export const API_BASEURL = 'http://localhost:8000';

export const getAccessToken = ():string|null => {
    const token = localStorage.getItem("access_token")
    return token
}


export const getRefreshToken = ():string|null => {
    const token = localStorage.getItem("refresh_token")
    return token
}

// setup axios configurations
export const getAxiosConfig = (token:string|null) => {
    return {
        headers:{
            'Content-type': 'multipart/form-data',
            accept: 'application/json',
            Authorization: token ? `Bearer ${token}` : ''
        }
    }
}