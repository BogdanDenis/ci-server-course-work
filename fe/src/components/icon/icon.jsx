import React from 'react';

const Icon = (props) => {
	const {
		icon,
		classes,
	} = props;
	const _classes = `fa fa-${icon} ${classes || ''}`;

	return <i className={_classes}></i>
};

export { Icon };
