import React from 'react';

import {
	Icon,
} from '../';

import './status.scss';

const statuses = {
	success: (props) => (
		<Icon
			icon="check-circle-o"
			classes={`${props.classes} status-icon success`}
			text={props.showText ? 'success' : ''}
		/>
	),
	fail: (props) => (
		<Icon
			icon="times-circle-o"
			classes={`${props.classes} status-icon fail`}
			text={props.showText ? 'fail' : ''}
		/>
	),
	pending: (props) => (
		<span className={`${props.classes} status-icon pending`}>
			<span className="status-icon__text">{props.showText ? 'pending' : ''}</span>
		</span>
	),
};

const Status = (props) => {
	const {
		status,
	} = props;

	return statuses[status](props) || null;
};

export { Status };
