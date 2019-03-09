import React from 'react';

import {
	Icon,
} from '../';

import './status.scss';

const statuses = {
	success: <Icon icon="check-circle-o" classes="status-icon success" />,
	fail: <Icon icon="times-circle-o" classes="status-icon fail" />,
	pending: <span className="status-icon pending">pending...</span>,
};

const Status = (props) => {
	const {
		status,
	} = props;

	return statuses[status] || null;
};

export { Status };
