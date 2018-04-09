import React from 'react';
import { Route, Switch } from 'react-router-dom';
import HomePage from "./components/HomePage";
import ProfilePage from "./components/profile/ProfilePage";

export default (
	<Switch>
		<Route exact path="/" component={HomePage} />
		<Route path="/profile/:number" component={ProfilePage} />
	</Switch>
);
