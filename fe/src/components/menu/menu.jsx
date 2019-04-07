import React, { Component } from 'react';
import classnames from 'classnames';

import { Icon } from '../../components';
import { LinkContainer } from '../';
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
						<LinkContainer href="/projects">
							<Icon icon={'code'}></Icon>
						</LinkContainer>
					</MenuItemContainer>
					<MenuItemContainer
						route={'/builds'}
					>
						<LinkContainer href="/builds">
							<Icon icon={'tasks'}></Icon>
						</LinkContainer>
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
