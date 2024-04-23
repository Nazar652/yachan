import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";


export default async function fetchThreads(category=null, page=null, pageSize=null) {
    try {
        let requestQuery = '?'
        if (category) {
          requestQuery += `category=${category}`
        }
        if (page) {
          requestQuery += `&page=${page}`
        }
        if (pageSize) {
          requestQuery += `&page_size=${pageSize}`
        }
        const requestUrl = `${host}/api/threads/${requestQuery}`
        const response = await axios.get(requestUrl)
        return response.data
    } catch (error) {
        console.error(error);
    }
}

