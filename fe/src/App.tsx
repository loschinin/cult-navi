import React, { useState } from "react";
import { MainContainer } from "./MainContainer";
import { Header } from "./components/Header";
import { MainInput } from "./components/MainInput";

export const MOCK_MUSEUMS = ["Art Museum", "Russian Museum"];
const App = () => {
  const [value, setValue] = useState<string | null>(MOCK_MUSEUMS[0]);
  return (
    <MainContainer>
      <Header value={value} setValue={setValue} />
      <MainInput selectedMuseum={value} />
    </MainContainer>
  );
};

export default App;
