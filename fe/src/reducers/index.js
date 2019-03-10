import { routerReducer } from 'react-router-redux';
import { combineReducers } from 'redux';

import { projectReducer } from './project-reducer';
import { buildReducer } from './build-reducer';

export const rootReducer = combineReducers({
	routing: routerReducer,
	project: projectReducer,
	build: buildReducer,
});
