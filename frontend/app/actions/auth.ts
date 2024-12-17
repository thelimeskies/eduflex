"use server"
import { SignUpFormSchema, FormState } from "@/lib/zod";
import { signUp } from "@/lib/auth";

export async function register(state: FormState, formData: FormData) {
	const firstname = formData.get("firstname") as string;
	const lastname = formData.get("lastname") as string;
	const email = formData.get("email") as string;
	const password = formData.get("password") as string;
	const confirm = formData.get("confirm") as string;
	
	const validated = SignUpFormSchema.safeParse(
		{
			firstname,
			lastname,
			email,
			password,
			confirm,
		}
	);

	if (!validated.success) {
		return { errors: validated.error.flatten().fieldErrors };
	}

	await signUp(email, password, confirm, firstname, lastname);
}
