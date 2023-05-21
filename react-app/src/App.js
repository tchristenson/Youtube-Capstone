import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import NewVideoPage from './components/NewVideoPage'
import SingleVideoPage from "./components/SingleVideoPage";
import SplashPage from "./components/SplashPage";
import EditVideoPage from "./components/EditVideoPage"
import UserProfilePage from "./components/UserProfilePage";
import ChannelPage from "./components/ChannelPage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/login" >
            <LoginFormPage />
          </Route>
          <Route exact path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/users/:userId">
            <UserProfilePage />
          </Route>
          <Route exact path="/videos/new">
            <NewVideoPage />
          </Route>
          <Route exact path="/videos/:videoId">
            <SingleVideoPage />
          </Route>
          <Route exact path="/videos/:videoId/edit">
            <EditVideoPage />
          </Route>
          <Route exact path="/channels/:channelId">
            <ChannelPage />
          </Route>
          <Route exact path="/">
            <SplashPage />
          </Route>
          <Route>
            Page Not Found
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
