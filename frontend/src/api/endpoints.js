import axios from 'axios';

const api = axios.create({
    baseURL: "http://127.0.0.1:5000/",
    headers: {
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin': "http://localhost:3000",
    },
    withCredentials: true
})

export const auth = async (details = null) => {

    return await api.post('/auth', details && details).then((response) => response).catch((error) => {
        return error.response
    })
}

export const refreshToken = async () => {
    return await api.get('/refresh_session').then((response) => response).catch((error) => {
        return error.response
    })
}
