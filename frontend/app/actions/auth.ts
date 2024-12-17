"use server"
import { SignUpFormSchema, FormState } from "@/lib/zod";
import { signUp, signIn } from "@/lib/auth";
import { redirect } from "next/navigation";

export async function register(state: FormState, formData: FormData) {
	const validated = SignUpFormSchema.safeParse(
		{
			email: formData.get("email") as string,
			password: formData.get("password") as string,
			confirm: formData.get("confirm") as string,
			firstname: formData.get("firstname") as string,
			lastname: formData.get("lastname") as string,
		}
	);

	if (!validated.success) {
		return { errors: validated.error.flatten().fieldErrors };
	}

	const { email, password, confirm, firstname, lastname } = validated.data;

	let user = await signUp(email, password, confirm, firstname, lastname);
	console.log(user);
	localStorage.setItem("user", JSON.stringify(user));

	redirect("/signin")
}

export async function login(state: FormState, formData: FormData) {
	const validated = SignUpFormSchema.safeParse(
		{
			email: formData.get("email") as string,
			password: formData.get("password") as string,
		}
	);

	if (!validated.success) {
		return { errors: validated.error.flatten().fieldErrors };
	}

	const { email, password } = validated.data;

	let user = await signIn(email, password);
	console.log(user);

	redirect("/signin")
}
