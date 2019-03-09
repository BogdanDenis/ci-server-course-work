import React from 'react';
import { connect } from 'react-redux';

import { ProjectPreview } from './project-preview';
import {
	setViewedProject,
} from '../../../../actions';

const ProjectPreviewContainer = connect(
	null,
	{
		setViewedProject,
	}
)(ProjectPreview);

export { ProjectPreviewContainer };
