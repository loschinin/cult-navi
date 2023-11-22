import React, { ReactNode } from "react";
import { createTheme, ThemeProvider } from "@mui/material/styles";

type Props = {
  children: ReactNode;
};

export const MuiProvider = ({ children }: Props) => {
  const theme = createTheme({
    components: {
      MuiPaper: {
        styleOverrides: {
          root: {
            backgroundColor: "#bdd9f3",
            minWidth: 350,
            maxWidth: 900,
            width: "100%",
          },
        },
      },
    },
  });
  return <ThemeProvider theme={theme}>{children}</ThemeProvider>;
};
