import React from 'react';
import classnames from 'classnames';

const MenuItem = (props) => {
	const {
		children,
		route,
		location,
	} = props;

	const active = location.pathname === route;

	const classes = classnames('list-group-item menu__item', {
		active,
	});

	return (
		<li className={classes}>
			{children}
		</li>
	);
};

export { MenuItem };
