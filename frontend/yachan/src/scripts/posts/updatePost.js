import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";

export default function updatePost() {
    const editPost = async (newData) => {
        try {
            const formData = new FormData();
            formData.append('updated_text', newData.updated_text);

            const response = await axios.patch(`${host}/api/posts/${newData.id}/`, formData, {
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
        editPost,
    };
}
