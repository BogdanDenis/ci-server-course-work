import React from 'react';
import { withRouter } from 'react-router-dom';

import { Link } from './link';

const LinkContainer = withRouter(props => <Link {...props} />);

export { LinkContainer };
