import React from 'react';

import { BuildPreviewContainer } from '../'

import './build-preview-list.scss';

const BuildPreviewList = ({ builds, }) => {
	return (
		<section className="build-preview-list">
			<h3 className="build-preview-list__heading">Builds:</h3>
			<ul className="list-group">
			{
				builds.map(build => {
					return (
						<li className="list-group-item" key={build.id }>
							<BuildPreviewContainer {...build} />
						</li>
					);
				})
			}
			</ul>
		</section>
		
	);
};

export { BuildPreviewList };
