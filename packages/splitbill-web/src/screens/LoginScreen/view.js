import { useState } from "react";
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../navigations';
import { Formik, Field } from "formik";
import {
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  FormErrorMessage,
  Input,
  VStack
} from "@chakra-ui/react";
import LineLogin from './components/LineLogin';
import 'reactjs-line-login/dist/index.css';

const LoginScreen = () => {
  const [payload, setPayload] = useState(null);
  const [idToken, setIdToken] = useState(null);
  let navigate = useNavigate();
  let location = useLocation();
  let auth = useAuth();

  let from = location.state?.from?.pathname || '/';

  function handleSubmit(event) {
    event.preventDefault();

    let formData = new FormData(event.currentTarget);
    let username = formData.get('username');

    auth.signin(username, () => {
      // Send them back to the page they tried to visit when they were
      // redirected to the login page. Use { replace: true } so we don't create
      // another entry in the history stack for the login page.  This means that
      // when they get to the protected page and click the back button, they
      // won't end up back on the login page, which is also really nice for the
      // user experience.
      navigate(from, { replace: true });
    });
  }

  return (
    <Flex bg="gray.100" align="center" justify="center" h="100vh">
      <Box bg="white" p={6} rounded="md">
        <LineLogin
        clientID='2006210817'
        clientSecret='0370031cdd35afb16fba1fa540990cbd'
        state='123445143131'
        redirectURI='http://10.141.31.70:4200/'
        scope='profile openid email' 
        setPayload={setPayload}
        setIdToken={setIdToken}
        />
      </Box>
    </Flex>
  );
};

export default LoginScreen;
