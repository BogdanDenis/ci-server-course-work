import React, { Component } from 'react';

import {
	Branch,
	Status,
	Steps,
	BuildPreviewList,
	Button,
	Icon,
} from '../../../../components';
import './project.scss';

class Project extends Component {
	constructor(props) {
		super(props);

		this.state = {
			inEditMode: false,
			settingsMenuOpen: false,
		};
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

	handleMenuClicked() {
		this.setState({
			settingsMenuOpen: !this.state.settingsMenuOpen,
		});
	}

	handleSettingsClicked() {
		this.setState({
			settingsMenuOpen: false,
			inEditMode: !this.state.inEditMode,
		});
	}

	render() {
		const {
			project,
		} = this.props;
		const {
			settingsMenuOpen,
			inEditMode,
		} = this.state;

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
				<Steps steps={steps} editMode={inEditMode}/>
				{this.renderBuildPreviews()}
				<div className="active-project__buttons">
					<Button
						classes="button-rebuild btn-warning"
						onClick={() => this.handleRebuildClick()}
					>
						Rebuild
					</Button>
					<Button
						onClick={() => this.handleMenuClicked()}
					>
						<Icon icon="ellipsis-v" version="5" />
					</Button>
					{
						settingsMenuOpen && (
							<div className="settings-buttons btn-group-vertical" role="group">
								<Button
									classes="btn btn-secondary btn-light settings-button"
									onClick={() => this.handleSettingsClicked()}
								>Edit</Button>
								<Button
									classes="btn btn-danger settings-button"
								>Delete</Button>
							</div>
						)
					}
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
