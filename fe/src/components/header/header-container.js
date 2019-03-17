import React from 'react';
import { push } from 'react-router-redux';
import { connect } from 'react-redux';

import { Header } from './header';

const HeaderContainer  = connect(
	null,
	{
		push,
	}
)(Header);

export { HeaderContainer };

