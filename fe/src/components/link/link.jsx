import React, { Component } from 'react';

import './link.scss';

class Link extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		const {
			href,
			classes,
			children
		} = this.props;

		return (
			<a
				href={href}
				className={`link ${classes}`}
			>{children}</a>
		);
	}
}

export { Link };
