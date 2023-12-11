import axios from "axios";

export const getMuseums = async () => {
  const response = await axios.get<string[]>("http://localhost:8000/museums", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  return response.data;
};

export const postPrompt = async (data: {
  name: string;
  prompt: string;
}) => {
  const response = await axios.post("http://localhost:8000/query", data);
  return response.data;
};
