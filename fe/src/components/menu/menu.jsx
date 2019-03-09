import React, { Component } from 'react';
import classnames from 'classnames';

import { Icon } from '../../components';
import { MenuItemContainer } from './menu-item-container';

import './menu.scss';

class Menu extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		const { location } = this.props;
		const classes = classnames('menu', {
			hide: location.pathname === '/login',
		});

		return (
			<nav className={classes}>
				<ul className="menu__list list list-group-item">
					<MenuItemContainer
						route={'/'}
					>
						<Icon icon={'code'}></Icon>
					</MenuItemContainer>
					<MenuItemContainer
						route={'/builds'}
					>
						<Icon icon={'tasks'}></Icon>
					</MenuItemContainer>
					<MenuItemContainer
						route={'/settings'}
					>
						<Icon icon={'cog'}></Icon>
					</MenuItemContainer>
				</ul>
			</nav>
		)
	}
}

export { Menu };
