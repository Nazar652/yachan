import axios from "axios";

const isAuthenticated = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/check-authentication/', {
      withCredentials: true
    });
    return response.data.isAuthenticated;
  } catch (error) {
    console.error(error);
    return false;
  }
};

export default isAuthenticated;