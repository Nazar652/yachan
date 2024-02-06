import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";


export default async function fetchThreads(category=null) {
  try {
    let requestUrl = category ? `${host}/api/threads/?category=${category}`: `${host}/api/threads`
    const response = await axios.get(requestUrl)
    return response.data
  } catch (error) {
    console.error(error);
  }
}