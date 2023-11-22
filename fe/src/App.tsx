import React from 'react';
import mainBg from './assets/mainBg.png';
import { Stack } from '@mui/material';
import { Autocomplete, TextField } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

function App() {
  return (
    <Stack sx={{backgroundImage: `url(${mainBg})`, backgroundSize: 'cover'}} height={'100vh'}>

        <Autocomplete freeSolo
        options={['option 1', 'option 2']}
        renderInput={params => (
          <TextField
            {...params}
            placeholder={'Select museum'}
            InputProps={{
              endAdornment: <SearchIcon sx={{ mr: 2 }} />,
            }}
          />
        )}
        fullWidth={true} />

    </Stack>
  );
}

export default App;
