import React from 'react';

const Icon = (props) => {
	const {
		icon,
		classes,
		text,
		version,
	} = props;
	const _classes = `${version !== 5 ? 'fa' : 'fas'} fa-${icon} ${classes || ''}`;

	return (
		<i className={_classes}>
			<span className="icon__text">{text}</span>
		</i>
	);
};

export { Icon };
