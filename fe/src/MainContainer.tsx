import React, { ReactNode } from "react";
import mainBg from "./assets/mainBg.png";
import { Stack } from "@mui/material";

type Props = {
  children: ReactNode;
};

export const MainContainer = ({ children }: Props) => {
  return (
    <Stack
      sx={{
        backgroundImage: `url(${mainBg})`,
        backgroundSize: "cover",
        backgroundPositionX: "center",
        backgroundAttachment: "fixed",
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
