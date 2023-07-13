import axios from 'axios';

export default function useNewThread() {
  const newThread = async (threadData) => {
    try {
      const formData = new FormData();
      formData.append('subject', threadData.subject);
      formData.append('text', threadData.text);
      formData.append('author_name', threadData.author_name);
      formData.append('category', threadData.category);
      formData.append('author', threadData.author);
      for (let i = 0; i < threadData.images.length; i++) {
        formData.append('images', threadData.images[i]);
      }

      const response = await axios.post('http://127.0.0.1:8000/api/threads/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  return {
    newThread,
  };
}
