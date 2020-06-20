import axios from 'axios';

export default function currentUser(token=null) {
    axios.defaults.headers.common['Authorization'] = token ? `token ${token}` : null
}