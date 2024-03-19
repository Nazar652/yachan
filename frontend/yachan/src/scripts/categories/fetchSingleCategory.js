import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";


export default async function fetchSingleCategory(category) {
    let requestUrl = `${host}/api/categories/${category}`
    const response = await axios.get(requestUrl)
    return response.data
}