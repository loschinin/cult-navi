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
  selectedMuseum: string;
  prompt: string;
}) => {
  const response = await axios.post("url", data);
  return response.data;
};
