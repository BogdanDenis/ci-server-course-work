import React, { Component } from 'react';
import { Route } from 'react-router-dom';

import {
	ProjectPreviewListContainer,
	ProjectContainer,
} from './components';
import { PREVIEW_PROJECT_ROUTE } from '../../constants/routes';

import './projects.scss';

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
				<ProjectPreviewListContainer />
				<Route
					path={PREVIEW_PROJECT_ROUTE}
					component={ProjectContainer}
				/>
			</section>
		);
	}
}

export { ProjectsPage };
