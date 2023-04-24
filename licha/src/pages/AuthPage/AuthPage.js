import { useEffect, useState } from 'react';
import { useForm } from 'react-hook-form';
import { useDispatch, useSelector } from 'react-redux';
import { Navigate } from 'react-router-dom';

import { Input } from '../../components/Input/Input';
import { Button } from '../../components/Button/Button';
import { FormControl } from '../../components/FormControl/FormControl';
import { authenticateUser } from '../../store/actions/auth';
import { useMutation } from '../../hooks/useMutation';

import './AuthPage.scss';

const baseUrl = 'http://127.0.0.1:8000/';
const apiKey = 'anfuvoufneunvinviufnisuvnsDUNv'

const LOG_IN_MODE = 'log-in';
const REGISTER_MODE = 'register';
const EMAIL_PATTERN = /^[a-zA-Z-._0-9]+@[a-z]+\.[a-z]{2,3}$/

const LOG_IN_FIELDS = [
	{
		as: Input,
		placeholder: "E-mail",
		type: "email",
		name: "email",
		label: "E-mail", 
		id: "email",
		rules: {
			required: "This is a required field",
			pattern: {
				value: EMAIL_PATTERN,
				message: "Email must has such template 'someText@email.com'"
			}
		}
	},
	{
		as: Input,
		placeholder: "Password",
		type: "password",
		name: "password",
		label: "Password", 
		id: "password",
		rules: {
			required: "This is a required field",
			minLength: {
				value: 8,
				message: 'Password should have minimum length of 8'
			}
		}
	}
];

const selectIdToken = state => !!state.auth.idToken;

export const AuthPage = () => {
	const [mode, setMode] = useState(LOG_IN_MODE);

	const isLogInMode = mode === LOG_IN_MODE;

	const { control, handleSubmit, formState: {errors}, formState, getValues, clearErrors, reset } = useForm({});

	const isAuthenticated = useSelector(selectIdToken);
	const dispatch = useDispatch();

	const authUrl = isLogInMode 
	? `/accounts:signInWithPassword?key=${apiKey}` 
	: `/accounts:signUp?key=${apiKey}`;

	const fullUrl = baseUrl + authUrl;
	const {mutate} = useMutation({
		url: fullUrl,
		headers: {
			'Content-Type': 'application/json'
		},
		onSuccess: response => {
			const { idToken, localId } = response;
			// Handle errors
			if (!idToken && !localId) return;
			dispatch(authenticateUser(idToken, localId))
		}
});

	useEffect(() => {
		reset();
		clearErrors();
	}, [mode, reset, clearErrors]);

	if (isAuthenticated) return <Navigate to="/"/>;

	const handleSwitchMode = () => {
		setMode(prevMode => (prevMode === LOG_IN_MODE ? REGISTER_MODE : LOG_IN_MODE));
	};

	const onSubmit = values => {
		mutate(JSON.stringify({...values, returnSecureToken: true}))
	}

	const onError = errors => console.log(errors);

	const REGISTER_FIELDS = [
		{
			as: Input,
			placeholder: "First name",
			type: "text",
			name: "firstName",
			label: "First name", 
			id: "first-name",
			rules: {
				required: "This is a required field"
			}
		},
		{
			as: Input,
			placeholder: "Last name",
			type: "text",
			name: "lastName",
			label: "Last name", 
			id: "last-name",
			rules: {
				required: "This is a required field"
			}
		},
		// {
		// 	as: Input,
		// 	placeholder: "Age",
		// 	type: "number",
		// 	name: "age",
		// 	label: "Age", 
		// 	id: "age",
		// 	rules: {
		// 		valueAsNumber: true
		// 	}
		// },
		{
			as: Input,
			placeholder: "E-mail",
			type: "email",
			name: "email",
			label: "E-mail", 
			id: "email",
			rules: {
				required: "This is a required field"
			}
		},
		{
			as: Input,
			placeholder: "Password",
			type: "password",
			name: "password",
			label: "Password", 
			id: "password",
			rules: {
				required: "This is a required field",
				minLength: {
					value: 8,
					message: 'Password should have minimum length of 8'
				}
			}
		},
		{
			as: Input,
			placeholder: "Confirm password",
			type: "password",
			name: "confirmPassword",
			label: "Confirm password", 
			id: "confirm-password",
			rules: {
				required: "This is a required field",
				validate: confirmPasswordValue => {
					const passwordValue = getValues('password')

					if(confirmPasswordValue === passwordValue) return null

					return 'Password and confirm password should match'
				}
			}
		} 
	];

	const fields = isLogInMode ? LOG_IN_FIELDS : REGISTER_FIELDS;

	const { isSubmitting } = formState;

	return (
		<div className="auth-page">
			<div className="auth-page__form-wrapper">
				<form autoComplete="off" noValidate className="auth-page__form" onSubmit={handleSubmit(onSubmit, onError)}>
					<fieldset className="auth-page__fieldset">
						<legend className="auth-page__legend">
							{isLogInMode ? 'Log in to your account' : 'Register'}
						</legend>
						{fields.map(({ id, ...other }) => (
						<FormControl 
						key={id}
						control={control}
						id={id} 
						className="auth-page__form-control"
						errors={errors}
						{...other} 
						/>
						))}
					</fieldset>
					<Button type='submit' className='auth-page__submit-button' disabled={isSubmitting}>
						{isLogInMode ? 'Log in' : 'Register'}
					</Button>
				</form>
				<div className='auth-page__note-wrapper'>
					<span>{isLogInMode ? `Don't have account?` : `Already have an account?`}</span>
					<Button className='auth-page__switch-button' onClick={handleSwitchMode}>
						{isLogInMode ? 'Create account' : 'Log in to your account'}
					</Button>
				</div>
			</div>
		</div>
	)
};