import React, { Component } from 'react';

import {
	Steps,
} from '../../../../components';

import './create-project.scss';

class CreateProject extends Component {
	constructor(props) {
		super(props);

		this.state = {
			key: '',
			name: '',
			repoPath: '',
			branch: '',
			pollTimeout: 0,
			steps: '',
		};
	}

	setStateField(field, value) {
		this.setState({
			[field]: value,
		});
	}

	createProject(e) {
		e.preventDefault();
		const {
			key,
			name,
			repoPath,
			branch,
			pollTimeout,
			steps,
		} = this.state;
		const { createProject } = this.props;

		const formData = {
			key,
			name,
			repoPath,
			branch,
			pollTimeout,
			steps,
		};

		createProject(formData);
	}

	saveSteps(steps) {
		this.setState({
			steps: steps.join(';;'),
		});
	}

	render() {
		const { steps } = this.state;

		const stepsArr = steps.split(';;');

		return (
			<section className="create-project">
				<h2 className="create-project__title">Create project</h2>
				<form className="create-project__form form" onSubmit={e => this.createProject(e)}>
					<div className="form-group">
						<label for="key">Project key</label>
						<input
							type="text"
							className="form-control"
							id="key"
							placeholder="Project key"
							onChange={e => this.setStateField('key', e.target.value)}
						/>
					</div>
					<div className="form-group">
						<label for="name">Project Name</label>
						<input
							type="text"
							className="form-control"
							id="name"
							placeholder="Project name"
							onChange={e => this.setStateField('name', e.target.value)}
						/>
					</div>
					<div className="form-group">
						<label for="repoPath">Path to repository directory</label>
						<input
							type="text"
							className="form-control"
							id="repoPath"
							placeholder="Repository path"
							onChange={e => this.setStateField('repoPath', e.target.value)}
						/>
					</div>
					<div className="form-group">
						<label for="branch">Branch</label>
						<input
							type="text"
							className="form-control"
							id="branch"
							placeholder="Branch"
							onChange={e => this.setStateField('branch', e.target.value)}
						/>
					</div>
					<div className="form-group">
						<label for="pollTimeout">Polling timeout (seconds)</label>
						<input
							type="number"
							min="1"
							className="form-control"
							id="pollTimeout"
							placeholder="Polling timeout"
							onChange={e => this.setStateField('pollTimeout', e.target.value)}
						/>
					</div>
					<Steps steps={stepsArr} editMode onStepsSave={steps => this.saveSteps(steps)} />
					<button type="submit" className="form__submit btn btn-primary">
						Create
					</button>
				</form>
			</section>
		);
	}
}

export { CreateProject };

