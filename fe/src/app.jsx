import React, { Component } from 'react';
import { Route, withRouter } from 'react-router';

import {
	LoginPage,
	ProjectsPageContainer,
} from './pages';
import {
	MenuContainer,
	Header,
	LinksNavigationContainer,
} from './components';
import * as routes from './constants/routes';

class App extends Component {
	render() {
		return (
			<>
				<MenuContainer />
				<Header />
				<div className="app">
					<Route
						exact
						path={routes.PROJECTS_ROUTE}
						component={ProjectsPageContainer}
					/>
					<Route
						path={routes.LOGIN_ROUTE}
						component={LoginPage}
					/>
				</div>
			</>
		);
	}
}

export default App = withRouter(App);
