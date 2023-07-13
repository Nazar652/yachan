import axios from 'axios';

export default async function fetchCategories() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/categories/');
    return response.data;
  } catch (error) {
    console.error(error);
  }
}
