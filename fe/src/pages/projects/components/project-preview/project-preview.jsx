import React, { Component } from 'react';

import {
	Branch,
	Status,
} from '../../../../components';
import { previewProjectRoute } from '../../../../helpers';

import './project-preview.scss';

class ProjectPreview extends Component {
	constructor(props) {
		super(props);
	}

	handleClick() {
		const {
			id,
			setViewedProject,
			push,
		} = this.props;

		setViewedProject(id);
		push(previewProjectRoute(id));
	}

	render() {
		const {
			name,
			id,
			status,
			branch,
		} = this.props;

		return (
			<li
				key={id}
				className="project-preview list-group-item d-flex align-items-center"
				onClick={() => this.handleClick()}
			>
				<Status status={status} />
				<h2 className="project-preview__name">{name}</h2>
				<Branch
					classes={'project-preview__branch'}
					branch={branch}
				/>
			</li>
		);
	}
}

export { ProjectPreview };
