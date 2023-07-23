import axios from 'axios';


export default async function fetchCategories(url) {
  try {
    const response = await axios.get(`${url}/api/categories`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}
