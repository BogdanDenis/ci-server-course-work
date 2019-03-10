import React from 'react';
import classnames from 'classnames';

import './output.scss';

const Output = ({ text = '', classes }) => {
	console.log(text.split(/\r?\n/));

	return (
		<pre className={classnames('output', classes)}>
			<output className="output__text">{text}</output>
		</pre>
	)
};

export { Output };
