import React, { useState } from "react";
import { IconButton, LinearProgress, Paper, Stack, TextField, Typography} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import ClearIcon from "@mui/icons-material/Clear";
import { useMutation } from "@tanstack/react-query";
import { postPrompt } from "../services";

interface ApiError {
  response: {
    data: {
      message: string;
      statusCode: number;
    };
  };
}

type Props = {
  name: string | null;
};
const INITIAL_MESSAGES: string[] = [];
export const MainInput = ({ name }: Props) => {
  const [messages, setMessages] = useState<string[]>(INITIAL_MESSAGES);
  const [prompt, setPrompt] = useState("");

  React.useEffect(() => {
    // Прокрутка страницы вниз при каждом обновлении значения 'messages'
    messages.length > 3 && window.scrollTo(0, document.body.scrollHeight);
  }, [messages]);

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

  const { mutate: mutatePrompt, isLoading: isMutatePromptLoading, error } = useMutation<{response: string}, ApiError, Parameters<typeof postPrompt>[0]>(postPrompt, {
    onSuccess: (data) => {
      setMessages((prevState) => [...prevState, data.response])
      console.log("postPrompt success", data.response);
    },
    onError: (error) => {
      console.log('onError:', error)
    }
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
          <Typography variant={"h6"} p={1} key={index} sx={{backgroundColor: index % 2 ? 'rgba(255,255,255,0.3)' : 'transparent'}}>
            {message}
          </Typography>
        ))}
        {isMutatePromptLoading && <LinearProgress/>}
        <Typography variant={'caption'} color={'mediumvioletred'}>{error?.response?.data?.message}</Typography>
        <TextField
          value={prompt}
          variant={'standard'}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder={"Ask AI..."}
          onKeyDown={handleKeyDown}
          disabled={isMutatePromptLoading}
          autoFocus
          InputProps={{
            endAdornment:
              <IconButton onClick={handleSendPrompt} disabled={isMutatePromptLoading}>
                 <SendIcon/>
              </IconButton>
          }}
          fullWidth
        />
      </Stack>
    </Paper>
  );
};
