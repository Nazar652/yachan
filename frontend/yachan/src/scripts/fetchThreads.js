import axios from 'axios';
import {hostname} from "@/scripts/globalVariables";


export default async function fetchThreads() {
  try {
    const response = await axios.get(`${hostname}/api/threads`)
    return response.data
  } catch (error) {
    console.error(error);
  }
}
