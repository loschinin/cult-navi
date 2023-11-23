import React, { ReactNode } from "react";
import shadow from "./assets/shadow.png";
import { Stack } from "@mui/material";

type Props = {
  children: ReactNode;
  background: string;
};

export const MainContainer = ({ children, background }: Props) => {
  return (
    <Stack
      sx={{
        backgroundImage: `url(${shadow}), url(${background})`,
        backgroundSize: "cover",
        backgroundPosition: "bottom",
        backgroundAttachment: "fixed",
        transition: "background-image 0.5s ease-in-out",
        boxShadow: "inset 0px 100px 100px 100px rgba(0, 0, 0, 0.65)",
      }}
      minHeight={"100vh"}
      alignItems={"center"}
      justifyContent={"space-between"}
      px={4}
      gap={1}
    >
      {children}
    </Stack>
  );
};
