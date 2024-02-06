export function setToken(token) {
    return localStorage.setItem('userToken', token)
}

export function getToken() {
    return localStorage.getItem('userToken')
}