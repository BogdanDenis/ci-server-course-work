import React, { Component } from 'react';
import classnames from 'classnames';

import {
	Button,
	Icon,
} from '../';
import './steps.scss';

class Steps extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		const {
			steps,
			classes,
			editMode,
		} = this.props;
	
	
		return (
			<section className={classnames('steps', classes)}>
				<h3 className="steps__heading">Steps:</h3>
				<ul className="steps__list">
					{
						steps.map((step) => {
							return (
								<li className='step'>
									{
										editMode ? (
											<div>
												<input type="text" value={step} onInput={e => console.log(e.target.value)}/>
												<Button classes="remove-step">
													<Icon icon="times" version="5" />
												</Button>
											</div>
										) : (step)
									}
								</li>
							);
						})
					}
				</ul>
				{
					editMode && (
						<Button classes="add-step" onClick={() => {}}>
							<Icon icon="plus" version="5" />
						</Button>
					)
				}
			</section>
		);
	}
}

export { Steps };
