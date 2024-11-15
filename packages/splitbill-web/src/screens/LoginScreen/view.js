import { useEffect, useState } from 'react';
import { useLiff } from 'react-liff';
import 'reactjs-line-login/dist/index.css';

const LoginScreen = () => {
  const [displayName, setDisplayName] = useState('');
  const { error, isLoggedIn, isReady, liff } = useLiff();


  useEffect(() => {
    if (!isLoggedIn) return;

    (async () => {
      const profile = await liff.getProfile();
      const token = await liff.getIDToken();
      console.log("🚀 ~ token:", token)
      console.log("🚀 ~ profile:", profile)
      setDisplayName(profile.displayName);
    })();
  }, [liff, isLoggedIn]);

  const showDisplayName = () => {
    if (error) return <p>Something is wrong.</p>;
    if (!isReady) return <p>Loading...</p>;

    if (!isLoggedIn) {
      return (
        <button className="App-button" onClick={liff.login}>
          Login
        </button>
      );
    }
    return (
      <>
        <p>Welcome to the react-liff demo app, {displayName}!</p>
        <button className="App-button" onClick={liff.logout}>
          Logout
        </button>
      </>
    );
  };

  return (
    <div className="App">
      <header className="App-header">{showDisplayName()}</header>
    </div>
  );
};

export default LoginScreen;
