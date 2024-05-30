import axios from 'axios';
import {host} from "@/scripts/global/globalVariables";
import {getToken} from "@/scripts/global/tokenUtils";

export default function updateThread() {
    const editThread = async (newData) => {
        const formData = new FormData();
        formData.append('updated_text', newData.updated_text);

        const response = await axios.patch(`${host}/api/threads/${newData.id}/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'usertoken': getToken()
            },
        });

        return response.data;
    };

    return {
        editThread,
    };
}
