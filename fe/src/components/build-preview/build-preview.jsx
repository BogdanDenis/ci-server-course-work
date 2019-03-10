import React, { Component } from 'react';

import {
	Branch,
	Status,
	TimePassed,
} from '../';
import { buildRoute } from '../../helpers/route-generators';
import './build-preview.scss';

class BuildPreview extends Component {
	constructor(props) {
		super(props);
	}

	handleBuildClick() {
		const {
			setActiveBuild,
			push,
			_id,
		} = this.props;

		setActiveBuild(_id);
		push(buildRoute(_id));
	}

	render() {
		const {
			_id,
			commitId,
			commitMessage,
			commitAuthor,
			endTime,
			branch,
			status,
		} = this.props;

		return (
			<div
				className="build-preview line-wrapper align-content-center"
				key={_id}
				onClick={() => this.handleBuildClick()}
			>
				<h4 className="build-preview__hash">{commitId}</h4>
				<Status status={status} showText />
				<Branch branch={branch} />
				<TimePassed startTime={endTime ? endTime.$date : null} />
			</div>
		);
	}
}

export { BuildPreview };
