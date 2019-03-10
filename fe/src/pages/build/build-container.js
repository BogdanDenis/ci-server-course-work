import React from 'react';
import { connect } from 'react-redux';

import { BuildPage } from './build';
import { setActiveBuild } from '../../actions';
import { selectActiveBuild } from '../../selectors';

const mapStateToProps = state => ({
	build: selectActiveBuild(state),
});

const BuildPageContainer = connect(
	mapStateToProps,
	{
		setActiveBuild,
	},
)(BuildPage);

export { BuildPageContainer };
