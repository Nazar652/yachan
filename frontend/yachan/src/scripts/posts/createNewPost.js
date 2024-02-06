import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";

export default function createNewPost() {
  const newPost = async (postData) => {
    try {
      const formData = new FormData();
      formData.append('subject', postData.subject);
      formData.append('text', postData.text);
      formData.append('author_name', postData.author_name);
      formData.append('thread', postData.thread);
      formData.append('author', postData.author);
      formData.append('is_op', postData.is_op);
      for (let i = 0; i < postData.uploaded_images.length; i++) {
        formData.append('uploaded_images', postData.uploaded_images[i]);
      }

      const response = await axios.post(`${host}/api/posts/`, formData, {
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
