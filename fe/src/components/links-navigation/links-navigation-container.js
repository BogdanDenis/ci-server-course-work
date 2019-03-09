import React from 'react';
import { withRouter } from 'react-router-dom';

import { LinksNavigation } from './links-navigation';

const LinksNavigationContainer = withRouter(props => <LinksNavigation {...props} />);

export { LinksNavigationContainer };
