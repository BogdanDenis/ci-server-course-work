import React from 'react';
import classnames from 'classnames';

import './button.scss';

const Button = ({ classes, onClick, children }) => (
	<button className={classnames('button btn', classes)} onClick={onClick}>
		{children}
	</button>
);

export { Button };
