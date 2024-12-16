"use client";

import SchoolOnboarding from "@/components/ui/school-onboarding";

export default function TestPage() {
  const handleOnboardingSubmit = (data: any) => {
    console.log("Form submitted:", data);
    // Add API call here if needed
  };

  return <SchoolOnboarding onSubmit={handleOnboardingSubmit} />;
}
