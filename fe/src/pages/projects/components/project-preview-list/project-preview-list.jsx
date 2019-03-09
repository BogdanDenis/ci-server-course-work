import React, { Component } from 'react';

import { ProjectPreviewContainer } from '../';

import './project-preview-list.scss';

class ProjectPreviewList extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		const {
			projects,
		} = this.props;

		return (
			<ul className="project-preview-list list-group">
			{
				projects.map(project => {
					const props = {
						...project,
						key: project.id,
						_key: project.key,
					};
	
					return <ProjectPreviewContainer {...props} />;
				})
			}
			</ul>
		);
	}
}

export { ProjectPreviewList };
