import axios from "axios";

export async function signUp(email: string, password1: string, password2: string, firstname: string, lastname: string) {
	try {
		const api = await axios.post("https://b3lst3wl-8000.uks1.devtunnels.ms/api/v1/auth/register/", {
			email: email,
			password1: password1,
			password2: password2,
			first_name: firstname,
			last_name: lastname
		}, {
			headers: {
				"Content-Type": "application/json",
			}
		});
		return api.data;

	} catch (error) {
		return error;
	}
}

export async function signIn(email: string, password1: string) {
	try {
		const api = await axios.post("https://b3lst3wl-8000.uks1.devtunnels.ms/api/v1/auth/login/", {
			email: email,
			password: password1,
		}, {
			headers: {
				"Content-Type": "application/json",
			}
		});
		return api.data;

	} catch (error) {
		return error;
	}
}