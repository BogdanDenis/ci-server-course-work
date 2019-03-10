import React from 'react';
import { connect } from 'react-redux';
import { push } from 'react-router-redux';

import { BuildPreview } from './build-preview';
import { setActiveBuild } from '../../actions';

const BuildPreviewContainer = connect(
	null,
	{
		setActiveBuild,
		push,
	}
)(BuildPreview);

export { BuildPreviewContainer };
