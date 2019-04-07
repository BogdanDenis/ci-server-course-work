import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { push } from 'react-router-redux';

import { Link } from './link';

const LinkContainer = withRouter(connect(
	null,
	{
		push,
	},
)(props => <Link {...props}/>));

export { LinkContainer };
