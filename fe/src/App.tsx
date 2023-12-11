import React, { useEffect, useState } from "react";
import { MainContainer } from "./MainContainer";
import { Header } from "./components/Header";
import { MainInput } from "./components/MainInput";
import mainBg from "./assets/mainBg.png";
import ermitazh from "./assets/ermitazh.png";
import faberzhe from "./assets/faberzhe.png";
import russian from "./assets/russian.png";
import garden from "./assets/garden.png";
import sculpture from "./assets/sculpture.png";
import chistakov from "./assets/chistakov.png";
import kuindzhi from "./assets/kuindzhi.png";
import erarta from "./assets/erarta.png";
import newMuseum from "./assets/new.png";
import shitglits from "./assets/shitglits.png";
import logo from "./assets/logo.png";
import {LinearProgress, Stack, Typography} from "@mui/material";
import {useQuery} from "@tanstack/react-query";
import {getMuseums} from "./services";

const preloadImages = () => {
  const images = [
    mainBg,
    ermitazh,
    faberzhe,
    russian,
    garden,
    sculpture,
    chistakov,
    kuindzhi,
    erarta,
    newMuseum,
    shitglits,
  ];
  images.forEach((image) => {
    const img = new Image();
    img.src = image;
  });
};
const museumsBackgrounds: Record<string, string> = {
  "Государственный Эрмитаж": ermitazh,
  "Музей Фаберже": faberzhe,
  "Государственный Русский музей": russian,
  "Летний сад": garden,
  "Государственный музей городской скульптуры": sculpture,
  "Музей-усадьба П. П. Чистякова": chistakov,
  "Музей-квартира А. И. Куинджи": kuindzhi,
  "Музей современного искусства Эрарта": erarta,
  "Новый музей": newMuseum,
  "Музей прикладного искусства СПбГХПА им.А.Л.Штиглица": shitglits,
};
const App = () => {
  useEffect(() => {
    preloadImages();
  }, []);

  const MOCK_MUSEUMS = Object.keys(museumsBackgrounds);
  const [value, setValue] = useState<string | null>(null);
  const { data: museums, isLoading: isMuseumsLoading } = useQuery(["museums"], getMuseums);

  console.log("museums:", museums);

  if (isMuseumsLoading) return <LinearProgress/>

  return (
    <MainContainer
      background={value ? museumsBackgrounds[value] || mainBg : mainBg}
    >
      <Header value={value} setValue={setValue} options={museums || MOCK_MUSEUMS} />
      <Stack gap={1} alignItems={"center"}>
        <img src={logo} alt={'logo'} width={200}/>
        <Typography variant={"h2"} color={"#ffffff"}>
          Cultural Neural Navi
        </Typography>
        <Typography variant={"h6"} color={"#d0d0d0"}>
          Your best Navigator by Saint-Petersburg Museums with Artificial
          Intelligence
        </Typography>
      </Stack>
      <MainInput name={value} />
    </MainContainer>
  );
};

export default App;
