import axios from 'axios';
import currentUser from './default';

const isAuthenticate = () => {
    const token = localStorage.getItem('auth-token')
    const user = localStorage.getItem('user')
    currentUser(token)
    return(token && user ? true : false)
}


const signup = (data) =>{
    return new Promise( (resolve, reject ) => {
        axios.post(
            "http://localhost:8000/api/account/signup/",
            {...data}
        ).then(resp => {
            if(resp.data.error){
                reject({success: false, error: resp.data.error})
            } else {
                localStorage.setItem('auth-token', resp.data.token)
                currentUser(resp.data.token)
                axios.get("http://localhost:8000/api/account/me/").then(resp => {
                    localStorage.setItem('user', JSON.stringify(resp.data))
                    resolve({success: true})
                }).catch(error => {
                    console.log(error)
                })
            }
        }).catch(error => {
            reject({success: false, error: error.response.statusText})
        })
    })
}


const login = (email, password) => (
    new Promise( (resolve, reject) => {
        axios.post(
            "http://localhost:8000/api/account/auth-token/",
			{"username": email, "password": password}
        ).then(resp => {
            localStorage.setItem('auth-token', resp.data.token)
            currentUser(resp.data.token)
            axios.get("http://localhost:8000/api/account/me/").then(resp => {
                localStorage.setItem('user', JSON.stringify(resp.data))
                resolve({success: true})
            }).catch(error => {
                console.log(error)
            })
        }).catch(error => {
            if (error.response && error.response.status === 400){
                reject('Wrong Email or Password')
			} else {
                reject('Server error !')
            }
        })
    })
)

const logout = (history) => {
    localStorage.clear()
    history.push('/login')
}


export {
    login,
    logout,
    signup,
    isAuthenticate
}