import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";



export default async function fetchCategories() {
  try {
    const response = await axios.get(`${host}/api/categories`)
    return response.data
  } catch (error) {
    console.error(error);
  }
}