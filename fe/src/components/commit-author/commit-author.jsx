import React from 'react';
import classnames from 'classnames';

import './commit-author.scss';

const CommitAuthor = ({ author, classes }) => {
	const regex = /^.+\((.+)\)$/g;
	const matchGroups = regex.exec(author);

	const email = matchGroups[1];
	const emailStartIndex = author.indexOf(email);
	const emailEndIndex = emailStartIndex + email.length;

	const authorBegin = author.substring(0, emailStartIndex);
	const authorEnd = author.substring(emailEndIndex);

	const href = `mailto:${email}`;

	return (
		<h4 className={classnames('author', classes)}>
			<span>Author: {authorBegin}</span>
			<a href={href} >{email}</a>
			<span>{authorEnd}</span>
		</h4>
	);
}

export { CommitAuthor };
