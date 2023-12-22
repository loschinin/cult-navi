import React, {useState} from "react";
import {Autocomplete, Paper, Stack, TextField} from "@mui/material";

type Props = {
  value: string | null;
  setValue(newValue: string | null): void;
  options: string[];
};
export const Header = ({ value, setValue, options }: Props) => {
  const [inputValue, setInputValue] = useState("");

  return (
    <Paper sx={{ p: 3, position: 'fixed', zIndex: 100 }}>
     <Stack direction={"row"} alignItems={"center"}>
        <Autocomplete
            value={value}
            onChange={(_, newValue: string | null) => {
              setValue(newValue);
            }}
            inputValue={inputValue}
            onInputChange={(event, newInputValue) => {
              setInputValue(newInputValue);
            }}
            options={options}
            renderInput={(params) => (
                <TextField {...params} label="Select Museum" fullWidth/>
            )}
            fullWidth
        />
      </Stack>
    </Paper>
  );
};
