import React, { Component } from 'react';
import { Route, withRouter } from 'react-router';

import {
	LoginPage,
} from './pages';
import * as routes from './constants/routes';

class App extends Component {
	render() {
		return (
			<div className="App">
				<Route
					exact
					path={routes.HOME_ROUTE}
					component={() => <h1>Home</h1>}
				/>
				<Route
					path={routes.LOGIN_ROUTE}
					component={LoginPage}
				/>
			</div>
		);
	}
}

export default App = withRouter(App);
