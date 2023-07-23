import axios from 'axios';
import {hostname} from "@/scripts/globalVariables";


export default async function fetchCategories() {
  try {
    const response = await axios.get(`${hostname}/api/categories`)
    return response.data
  } catch (error) {
    console.error(error);
  }
}
