import React from 'react';
import { connect } from 'react-redux';

import { ProjectsPage } from './projects';
import { getProjects } from '../../actions';

const ProjectsPageContainer = connect(
	null,
	{
		getProjects,
	}
)(ProjectsPage);

export { ProjectsPageContainer };
