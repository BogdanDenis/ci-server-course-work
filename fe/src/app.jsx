import React, { Component } from 'react';
import { Route, withRouter } from 'react-router';

import {
	LoginPage,
	ProjectsPageContainer,
	BuildPageContainer,
} from './pages';
import {
	MenuContainer,
	HeaderContainer,
} from './components';
import * as routes from './constants/routes';

class App extends Component {
	render() {
		return (
			<>
				<MenuContainer />
				<HeaderContainer />
				<div className="app">
					<Route
						path={routes.PROJECTS_ROUTE}
						component={ProjectsPageContainer}
					/>
					<Route
						path={routes.LOGIN_ROUTE}
						component={LoginPage}
					/>
					<Route
						path={routes.BUILD_ROUTE}
						component={BuildPageContainer}
					/>
				</div>
			</>
		);
	}
}

export default App = withRouter(App);
