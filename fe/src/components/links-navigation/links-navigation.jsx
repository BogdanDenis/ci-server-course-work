import React, { Component } from 'react';
import classnames from 'classnames';

import { LinkContainer } from '../../components';

import './links-navigation.scss';

class LinksNavigation extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		const {
			location,
		} = this.props;

		const classes = classnames('links-navigation', {
			hide: location.pathname === '/login',
		});

		return (
			<nav className={classes}>links</nav>
		)
	}
}

export { LinksNavigation };
