import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";

export default async function deletePost(postId) {
    const csrfToken = document.cookie.split('=')[1];
    try {
        const response = await axios.delete(`${host}/api/posts/${postId}/`, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'X-CSRFToken': csrfToken
            },
            withCredentials: true
        });

        return response.data;
    } catch (error) {
        console.error(error);
        throw error;
    }
}
