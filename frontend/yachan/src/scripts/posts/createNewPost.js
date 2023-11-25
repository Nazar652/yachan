import axios from 'axios';
import {hostname} from "@/scripts/global/globalVariables";

export default function createNewPost() {
  const newPost = async (postData, url) => {
    try {
      const formData = new FormData();
      formData.append('subject', postData.subject);
      formData.append('text', postData.text);
      formData.append('author_name', postData.author_name);
      formData.append('thread', postData.thread);
      formData.append('author', postData.author);
      for (let i = 0; i < postData.uploaded_images.length; i++) {
        formData.append('uploaded_images', postData.uploaded_images[i]);
      }

      const response = await axios.post(`${hostname}/api/posts/`, formData, {
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
    newPost,
  };
}
