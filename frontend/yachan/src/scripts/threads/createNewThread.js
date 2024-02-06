import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";

export default function createNewThread() {
    const newThread = async (threadData) => {
        try {
            const formData = new FormData();
            formData.append('subject', threadData.subject);
            formData.append('text', threadData.text);
            formData.append('author_name', threadData.author_name);
            formData.append('category', threadData.category);
            formData.append('author', threadData.author);
            for (let i = 0; i < threadData.uploaded_images.length; i++) {
                formData.append('uploaded_images', threadData.uploaded_images[i]);
            }

            const response = await axios.post(`${host}/api/threads/`, formData, {
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
