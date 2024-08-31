import { StrictMode } from 'react';
import { Provider } from "react-redux";
import * as ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import configureStore from "./store/configureStore";

const root = ReactDOM.createRoot(document.getElementById('root'));
const store = configureStore();

root.render(
  <Provider store={store}>
    <StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </StrictMode>
  </Provider>
);
