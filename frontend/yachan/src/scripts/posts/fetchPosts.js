import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";


export default async function fetchPosts(thread=null) {
  try {
    let requestUrl = thread ? `${host}/api/posts/?thread=${thread}`: `${host}/api/posts`
    const response = await axios.get(requestUrl)
    return response.data
  } catch (error) {
    console.error(error);
  }
}