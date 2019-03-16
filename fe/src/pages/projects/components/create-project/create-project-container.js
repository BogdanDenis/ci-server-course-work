import React from 'react';
import { connect } from 'react-redux';

import { CreateProject } from './create-project';
import {
	createProject,
} from '../../../../actions';

const CreateProjectContainer = connect(
	null,
	{
		createProject,
	},
)(CreateProject);

export { CreateProjectContainer };

