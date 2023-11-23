import React, { useState } from "react";
import { MainContainer } from "./MainContainer";
import { Header } from "./components/Header";
import { MainInput } from "./components/MainInput";

export const MOCK_MUSEUMS = [
  "Государственный Эрмитаж",
  "Музей Фаберже",
  "Государственный Русский музей",
  "Летний сад",
  "Государственный музей городской скульптуры",
  "Музей-усадьба П. П. Чистякова",
  "Музей-квартира А. И. Куинджи",
  "Музей современного искусства Эрарта",
  "Новый музей",
  "Музей прикладного искусства СПбГХПА им.А.Л.Штиглица",
];
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
