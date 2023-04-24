import PT from 'prop-types';
import cn from 'classnames';
import { Controller } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';

import './FormControl.scss';

export const FormControl = ({ className, label, id, as: Component, control, errors, name, rules, ...other }) => (
	<div className={cn('form-control', className)}>
		<label className='form-control__label' htmlFor={id}>{label}</label>
		<div className='form-control__field'>
			<Controller control={control} rules={rules} name={name} defaultValue='' render={({field}) => (
				<Component id={id} {...field } {...other}/>
			)}/>
			<ErrorMessage 
			errors={errors}
			name={name} 
			as={<span className='form-control__error'/>}
			/>
		</div>
	</div>
);

FormControl.propTypes = {
	// Form control field component
	as: PT.elementType.isRequired,
	// Additinal form control class name
	className: PT.string,
	// Form control's label content
	label: PT.node.isRequired,
	// Unique id used in label tag
	id: PT.string.isRequired,
	// Unique field name
	name: PT.string.isRequired,
	// Validation rules for the 'Controller'
	rules: PT.object,
	// Control from 'react-hook-form'
	control: PT.object.isRequired,
	// Errors from react-hook-form
	errors: PT.object.isRequired,
};