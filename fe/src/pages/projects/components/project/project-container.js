import React from 'react';
import { connect } from 'react-redux';

import { Project } from './project';
import {
	getProjectsBuilds,
	setViewedProject,
	rebuildProject,
	updateProjectSteps,
} from '../../../../actions';
import { selectActiveProject } from '../../../../selectors';

const mapStateToProps = state => ({
	project: selectActiveProject(state),
});

const ProjectContainer = connect(
	mapStateToProps,
	{
		getProjectsBuilds,
		setViewedProject,
		rebuildProject,
		updateProjectSteps,
	},
)(Project);

export { ProjectContainer };
