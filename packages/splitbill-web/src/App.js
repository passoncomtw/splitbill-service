import * as React from "react";
import { LiffProvider } from 'react-liff';
import {
  Route,
  Routes,
} from "react-router-dom";
import { AuthProvider, Layout, RequireAuth } from "./navigations";
import HomeScreen from "./screens/HomeScreen";
import LoginScreen from "./screens/LoginScreen";
import PublicScreen from "./screens/PublicScreen";

export default function App() {
  return (
    <LiffProvider liffId={'2006210817-n91Gao5j'}>
    <AuthProvider>
      <Routes>
        <Route exact element={<Layout />}>
          <Route path="/" element={<PublicScreen />} />
          <Route path="/login" element={<LoginScreen />} />
          <Route
            path="/protected"
            element={
              <RequireAuth>
                <HomeScreen />
              </RequireAuth>
            }
          />
        </Route>
      </Routes>
    </AuthProvider>
    </LiffProvider>
  );
}
