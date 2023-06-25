import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import SingleVideoPage from "./components/SingleVideoPage";
import SplashPage from "./components/SplashPage";
import UserProfilePage from "./components/UserProfilePage";
import ChannelPage from "./components/ChannelPage";
import Footer from "./components/Footer";
import UserPlaylistsPage from "./components/UserPlaylistsPage";
import SearchResults from "./components/SearchResults";

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
            <Route exact path="/users/:userId">
              <UserProfilePage />
            </Route>
            <Route exact path="/users/:userId/playlists/:playlistId">
              <UserPlaylistsPage />
            </Route>
            <Route exact path="/videos/:videoId">
              <SingleVideoPage />
            </Route>
            <Route exact path="/channels/:channelId">
              <ChannelPage />
            </Route>
            <Route exact path="/">
              <SplashPage />
            </Route>
            <Route exact path="/search">
              <SearchResults />
            </Route>
            <Route>
              Page Not Found
            </Route>
        </Switch>
      )}
      <Footer isLoaded={isLoaded} />
    </>
  );
}

export default App;
