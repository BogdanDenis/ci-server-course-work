import React from 'react';
import { connect } from 'react-redux';
import { push } from 'react-router-redux';

import { ProjectPreview } from './project-preview';
import {
	setViewedProject,
} from '../../../../actions';

const ProjectPreviewContainer = connect(
	null,
	{
		setViewedProject,
		push,
	}
)(ProjectPreview);

export { ProjectPreviewContainer };
