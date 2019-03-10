import React from 'react';
import classnames from 'classnames';

import { Icon } from '../';

import './branch.scss';

const Branch = (props) => {
	const {
		classes,
		branch,
	} = props;

	return (
		<div className={classnames(classes, 'branch d-flex align-items-center')}>
			<Icon icon="code-fork" classes="branch__icon" />
			<p className="branch__name">{branch}</p>				
		</div>
	);
}

export { Branch };
