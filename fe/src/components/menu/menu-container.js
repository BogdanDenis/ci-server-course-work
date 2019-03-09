import React from 'react';
import { withRouter } from 'react-router-dom';

import { Menu } from './menu';

const MenuContainer = withRouter(props => <Menu {...props} />);

export { MenuContainer };
