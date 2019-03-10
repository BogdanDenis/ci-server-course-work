import React from 'react';
import classnames from 'classnames';

import './steps.scss';

const Steps = (props) => {
	const {
		steps,
		classes,
	} = props;


	return (
		<section className={classnames('steps', classes)}>
			<h3 className="steps__heading">Steps:</h3>
			<ul className="steps__list">
				{
					steps.map((step) => {
						return (
							<li className='step'>{step}</li>
						);
					})
				}
			</ul>
		</section>
	);
};

export { Steps };
