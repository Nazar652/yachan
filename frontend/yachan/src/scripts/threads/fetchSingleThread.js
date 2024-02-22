import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";


export default async function fetchSingleThread(threadId) {
    let requestUrl = `${host}/api/threads/${threadId}`
    const response = await axios.get(requestUrl)
    return response.data
}