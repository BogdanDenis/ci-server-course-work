import React from 'react';
import { connect } from 'react-redux';

import { Project } from './project';

const ProjectContainer = connect(
	null,
	null,
)(Project);

export { ProjectContainer };
