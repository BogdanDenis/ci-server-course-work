import React from 'react';
import { connect } from 'react-redux';

import { ProjectPreviewList } from './project-preview-list';

const mapStateToProps = state => ({
	projects: state.project.projects,
});

const mapDispatchToProps = {};

const ProjectPreviewListContainer = connect(
	mapStateToProps,
	mapDispatchToProps,
)(ProjectPreviewList);

export { ProjectPreviewListContainer };
