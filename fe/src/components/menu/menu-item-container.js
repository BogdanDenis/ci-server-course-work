import React from 'react';
import { withRouter } from 'react-router-dom';

import { MenuItem } from './menu-item';

const MenuItemContainer = withRouter(props => <MenuItem {...props} />);

export { MenuItemContainer };
