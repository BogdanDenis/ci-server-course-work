import * as routes from '../constants/routes';

export const previewProjectRoute = (id) => routes.PREVIEW_PROJECT_ROUTE.replace(':projectId', id);
export const buildRoute = (id) => routes.BUILD_ROUTE.replace(':buildId', id);
