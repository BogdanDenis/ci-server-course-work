import React, { Component } from 'react';
import { Route } from 'react-router-dom';

import {
	ProjectPreviewListContainer,
	ProjectContainer,
	CreateProjectContainer,
} from './components';
import {
	PREVIEW_PROJECT_ROUTE,
	CREATE_PROJECT_ROUTE,
} from '../../constants/routes';

import './projects.scss';

const notCreateProjectRoute = /\/projects(?!\/create$).*/;

class ProjectsPage extends Component {
	constructor(props) {
		super(props);
	}

	componentDidMount() {
		const { getProjects } = this.props;

		getProjects();
	}

	render() {
		return (
			<section className="projects-page">
				<Route
					path={notCreateProjectRoute}
					component={ProjectPreviewListContainer}
				/>
				<Route
					path={PREVIEW_PROJECT_ROUTE}
					component={ProjectContainer}
				/>
				<Route
					path={CREATE_PROJECT_ROUTE}
					component={CreateProjectContainer}
				/>
			</section>
		);
	}
}

export { ProjectsPage };
