import PT from 'prop-types';
import cn from 'classnames';

import './Input.scss';

const DEFAULT_TYPE = 'text';
const DEFAULT_AUTOCOMPLETE = 'off';

export const Input = ({type = DEFAULT_TYPE, autoComplete=DEFAULT_AUTOCOMPLETE, className, ...other}) => (
	<input 
		{...other} 
		type={type} 
		autoComplete={autoComplete} 
		className={cn('input', className)}
	/>
);

Input.propTypes ={
	// Type of input
	type: PT.oneOf(['text', 'email', 'password', 'number']),
	// Additional input's className
	className: PT.string,
}