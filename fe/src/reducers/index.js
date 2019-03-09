import { routerReducer } from 'react-router-redux';
import { combineReducers } from 'redux';

import { projectReducer } from './project-reducer';

export const rootReducer = combineReducers({
	routing: routerReducer,
	project: projectReducer,
});
