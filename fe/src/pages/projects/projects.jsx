import React, { Component } from 'react';

import {
	ProjectPreviewListContainer,
} from './components';

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
			</section>
		);
	}
}

export { ProjectsPage };
