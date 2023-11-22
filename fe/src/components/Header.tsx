import React, { useState } from "react";
import {
  Autocomplete,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import { useQuery } from "@tanstack/react-query";
import { getMuseums } from "../services";
import { MOCK_MUSEUMS } from "../App";

type Props = {
  value: string | null;
  setValue(newValue: string | null): void;
};
export const Header = ({ value, setValue }: Props) => {
  const [inputValue, setInputValue] = useState("");

  const { data: museums } = useQuery(["museums"], getMuseums);

  console.log("museums:", museums);

  return (
    <Paper sx={{ p: 3 }}>
      <Stack
        direction={"row"}
        gap={3}
        flexWrap={"wrap"}
        alignItems={"center"}
        justifyContent={"space-between"}
      >
        <Autocomplete
          value={value}
          onChange={(_, newValue: string | null) => {
            setValue(newValue);
          }}
          inputValue={inputValue}
          onInputChange={(event, newInputValue) => {
            setInputValue(newInputValue);
          }}
          options={MOCK_MUSEUMS}
          renderInput={(params) => (
            <TextField {...params} label="Select Museum" fullWidth />
          )}
          fullWidth
          sx={{ maxWidth: 430 }}
        />
        <Stack gap={1}>
          <Typography variant={"h4"} color={"#010e33"}>
            Cultural Museum Navigator
          </Typography>
          <Typography variant={"caption"} color={"#102b75"}>
            Your favorite guide by Museums with Artificial Intelligence
          </Typography>
        </Stack>
      </Stack>
    </Paper>
  );
};
