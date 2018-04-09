import React from 'react';
import { Route, Switch } from 'react-router-dom';
import HomePage from "./components/HomePage";

export default (
	<Switch>
		<Route exact path="/" component={HomePage} />
	</Switch>
);
