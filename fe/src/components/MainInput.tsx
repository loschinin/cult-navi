import React, { useState } from "react";
import { IconButton, Paper, Stack, TextField, Typography } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import ClearIcon from "@mui/icons-material/Clear";
import { useMutation } from "@tanstack/react-query";
import { postPrompt } from "../services";

type Props = {
  name: string | null;
};
const INITIAL_MESSAGES: string[] = [];
export const MainInput = ({ name }: Props) => {
  const [messages, setMessages] = useState<string[]>(INITIAL_MESSAGES);
  const [prompt, setPrompt] = useState("");

  const handleSendPrompt = () => {
    console.log("prompt:", prompt);
    console.log("selectedMuseum:", name);
    setMessages((prevState) => [...prevState, prompt]);
    setPrompt("");
    mutatePrompt({ name: name || '', prompt });
  };
  const handleKeyDown = (event: { key: string }) => {
    if (event.key === "Enter") {
      handleSendPrompt();
    }
  };

  const { mutate: mutatePrompt } = useMutation(postPrompt, {
    onSuccess: (data) => {
      setMessages((prevState) => [...prevState, data.response])
      console.log("postPrompt success", data.response);
    },
  });

  return (
    <Paper sx={{ p: 3 }}>
      <Stack gap={3}>
        {!!messages.length && (
          <Stack
            direction={"row"}
            gap={1}
            alignItems={"center"}
            justifyContent={"flex-end"}
          >
            <Typography variant={"caption"}>Clear History</Typography>
            <IconButton onClick={() => setMessages(INITIAL_MESSAGES)}>
              <ClearIcon />
            </IconButton>
          </Stack>
        )}
        {messages.map((message, index) => (
          <Typography variant={"h6"} key={index}>
            {message}
          </Typography>
        ))}
        <TextField
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder={"Message AI..."}
          onKeyDown={handleKeyDown}
          InputProps={{
            endAdornment: (
              <IconButton onClick={handleSendPrompt}>
                <SendIcon />
              </IconButton>
            ),
          }}
          fullWidth
        />
      </Stack>
    </Paper>
  );
};
