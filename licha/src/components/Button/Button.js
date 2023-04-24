import PT from 'prop-types';
import cn from 'classnames';

import './Button.scss';

const DEFAULT_TYPE = 'button';
const DEFAULT_VARIANT = 'primery';

export const Button = ({type = DEFAULT_TYPE, variant = DEFAULT_VARIANT, className, children, ...other}) => (
	<button {...other} type={type} className={cn('button', `button--${variant}`, className)}>
		{children}
	</button>
)

Button.propTypes ={
	// Type of button
	type: PT.oneOf(['button', 'submit', 'reset']),
	// Variant of button's styling
	variant: PT.oneOf(['primary', 'secondary']),
	// Additional button's className
	className: PT.string,
	// Button's content
	children: PT.node.isRequired
}