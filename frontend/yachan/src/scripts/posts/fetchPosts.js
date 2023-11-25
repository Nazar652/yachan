import axios from 'axios';
import {hostname} from "@/scripts/global/globalVariables";


export default async function fetchPosts(thread=null) {
  try {
    let requestUrl = thread ? `${hostname}/api/posts/?thread=${thread}`: `${hostname}/api/posts`
    const response = await axios.get(requestUrl)
    return response.data
  } catch (error) {
    console.error(error);
  }
}