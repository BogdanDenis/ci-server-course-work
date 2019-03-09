import React, { Component } from 'react';

import {
	Icon,
	Status,
} from '../../../../components';

import './project-preview.scss';

class ProjectPreview extends Component {
	constructor(props) {
		super(props);
	}

	handleClick() {
		const {
			id,
			setViewedProject,
		} = this.props;

		setViewedProject(id);
	}

	render() {
		const {
			name,
			id,
			_key,
			status,
			branch,
		} = this.props;

		const _status = 'success';

		return (
			<li
				key={id}
				className="project-preview list-group-item d-flex align-items-center"
				onClick={() => this.handleClick()}
			>
				<Status status={_status} />
				<h2 className="project-preview__name">{_key}</h2>
				<div className="project-preview__branch branch d-flex align-items-center">
					<Icon icon="code-fork" classes="branch__icon" />
					<p className="branch__name">{branch}</p>				
				</div>
			</li>
		);
	}
}

export { ProjectPreview };
