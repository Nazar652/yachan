import axios from 'axios';
import {hostname} from "@/scripts/global/globalVariables";


export default async function fetchThreads(category=null) {
  try {
    let requestUrl = category ? `${hostname}/api/threads/?category=${category}`: `${hostname}/api/threads`
    const response = await axios.get(requestUrl)
    return response.data
  } catch (error) {
    console.error(error);
  }
}