import { StrictMode } from 'react';
import { Provider } from "react-redux";
import * as ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import configureStore from "./store/configureStore";
import { ChakraProvider } from '@chakra-ui/react'

const root = ReactDOM.createRoot(document.getElementById('root'));
const store = configureStore();

console.log("🚀 ~ process.env.REACT_APP_DOMAIN:", process.env.REACT_APP_DOMAIN)
root.render(
  <Provider store={store}>
    <StrictMode>
      <BrowserRouter>
        <ChakraProvider>
          <App />
        </ChakraProvider>
      </BrowserRouter>
    </StrictMode>
  </Provider>
);
