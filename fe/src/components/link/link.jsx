import React, { Component } from 'react';

import './link.scss';

class Link extends Component {
	constructor(props) {
		super(props);
	}

	redirect(e) {
		e.preventDefault();

		const {
			href,
			push,
		} = this.props;

		push(href);
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
				onClick={e => this.redirect(e)}
			>{children}</a>
		);
	}
}

export { Link };
