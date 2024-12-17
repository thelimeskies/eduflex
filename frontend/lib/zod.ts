import { z } from "zod";

export const SignUpFormSchema = z.object({
	firstname: z
		.string()
		.min(2, "Name is too short")
		.trim(),
	lastname: z
		.string()
		.min(2, "Name is too short")
		.trim(),
	email: z.string().email({message: "Invalid email address"}),
	password: z
		.string()
		.min(6, "Password must be at least 6 characters long")
		.trim(),
	confirm: z
	.string()
	.min(6)
	.trim(),
}).superRefine(({confirm, password}, ctx) => {
	if (password !== confirm) {
		ctx.addIssue({
			code: "custom",
			message: "Passwords do not match",
			path: ["confirm"],
		});
	}
});

export type FormState =
  | {
      errors?: {
        firstname?: string[]
        lastname?: string[]
        email?: string[]
        password?: string[]
				confirm?: string[]
      }
      message?: string
    }
  | undefined
