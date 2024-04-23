import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";


export default async function fetchPosts(thread=null, page=null) {
  try {
    let requestQuery = '?'
    if (thread) {
      requestQuery += `thread=${thread}`
    }
    if (page) {
      requestQuery += `&page=${page}`
    }
    const requestUrl =  `${host}/api/posts/${requestQuery}`
    const response = await axios.get(requestUrl)
    return response.data
  } catch (error) {
    console.error(error);
  }
}