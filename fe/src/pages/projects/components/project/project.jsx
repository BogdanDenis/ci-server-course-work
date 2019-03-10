import React, { Component } from 'react';

import {
	Branch,
	Status,
	Steps,
	BuildPreviewList,
	Button,
} from '../../../../components';
import './project.scss';

class Project extends Component {
	constructor(props) {
		super(props);
	}

	trySetViewedProject() {
		this.setViewedProjectTimeout = setTimeout(() => {
			const {
				getProjectsBuilds,
				setViewedProject,
				project,
				location,
			} = this.props;
	
			if (!project) {
				const projectId = location.pathname.split('/')[2];
				setViewedProject(projectId);
				this.trySetViewedProject();
			} else {
				clearTimeout(this.setViewedProjectTimeout);
				getProjectsBuilds(project.id);
			}
		}, 200);
	}

	componentDidMount() {
		const {
			getProjectsBuilds,
			project,
		} = this.props;

		if (!project) {
			this.trySetViewedProject();
			return;
		}

		getProjectsBuilds(project.id);
	}

	handleRebuildClick() {
		const {
			project,
			rebuildProject,
		} = this.props;

		rebuildProject(project.id);
	}

	render() {
		const {
			project,
		} = this.props;

		if (!project) {
			return null;
		}

		const steps = project.steps.split(';;').map(step => {
			return step;
		});

		return (
			<section className="active-project">
				<h2 className="active-project__name">{project.name}</h2>
				<div className="line-wrapper">
					<Branch
						classes={'active-project__branch line-item'}
						branch={project.branch}
					/>
					<Status
						status={project.status}
						showText
						classes={'line-item'}
					></Status>
				</div>
				<Steps steps={steps} />
				{this.renderBuildPreviews()}
				<div className="active-project__buttons">
					<Button
						classes="button-rebuild btn-warning"
						onClick={() => this.handleRebuildClick()}
					>
						Rebuild
					</Button>
				</div>
			</section>
		);
	}

	renderBuildPreviews() {
		const { project } = this.props;
		const builds = project.builds
			.filter(build => build.id !== undefined)
			.sort((a, b) => {
				const startTimeA = a.startTime ? a.startTime.$date : 0;
				const startTimeB = b.startTime ? b.startTime.$date : 0;

				if (startTimeA > startTimeB) return -1;
				if (startTimeA < startTimeB) return 1;
				return 0;
			})
			.map(build => ({
				...build,
				branch: project.branch,
			}));

		return <BuildPreviewList builds={builds} />;
	}
}

export { Project };
