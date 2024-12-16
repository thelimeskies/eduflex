"use client";

import { useState } from "react";

const idTypes = ["National ID", "International Passport", "Driver License", "Voter Card"];

export default function ParentOnboarding({ onSubmit }: { onSubmit: (data: any) => void }) {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState({
    phone: "",
    address: "",
    occupation: "",
    kyc: {
      annual_income: "",
      employer: "",
      designation: "",
      bank_account_statement: "",
      id_type: "",
      id_number: "",
      id_front: null as File | null,
      id_back: null as File | null,
    },
  });

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;

    if (currentStep === 1) {
      setFormData({ ...formData, [name]: value });
    } else {
      setFormData({
        ...formData,
        kyc: { ...formData.kyc, [name]: value },
      });
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name } = e.target;
    const file = e.target.files ? e.target.files[0] : null;

    setFormData({
      ...formData,
      kyc: { ...formData.kyc, [name]: file },
    });
  };

  const handleNext = () => {
    if (currentStep === 1 && (!formData.phone || !formData.address || !formData.occupation)) {
      alert("Please fill in all required fields in Basic Info.");
      return;
    }
    setCurrentStep(2);
  };

  const handleBack = () => setCurrentStep(1);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);
    // Remove onSubmit call temporarily
  };
  

//   const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
//     e.preventDefault();

//     if (
//       currentStep === 2 &&
//       (!formData.kyc.annual_income ||
//         !formData.kyc.employer ||
//         !formData.kyc.designation ||
//         !formData.kyc.bank_account_statement ||
//         !formData.kyc.id_type ||
//         !formData.kyc.id_number ||
//         !formData.kyc.id_front)
//     ) {
//       alert("Please fill in all required fields in KYC Info.");
//       return;
//     }

//     console.log("Form Data Submitted:", formData);
//     onSubmit(formData); // Pass form data to parent component or API
//   };

  return (
    <section className="max-w-3xl mx-auto mt-10 bg-gray-800 p-8 rounded-lg shadow-lg text-gray-200">
      <h2 className="text-3xl font-semibold mb-6 text-center">Parent Onboarding</h2>
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Step 1: Basic Info */}
        {currentStep === 1 && (
          <>
            <div>
              <label className="block mb-2">Phone *</label>
              <input
                type="text"
                name="phone"
                value={formData.phone}
                onChange={handleInputChange}
                placeholder="Your phone number"
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              />
            </div>
            <div>
              <label className="block mb-2">Address *</label>
              <textarea
                name="address"
                value={formData.address}
                onChange={handleInputChange}
                placeholder="Your address"
                rows={3}
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              ></textarea>
            </div>
            <div>
              <label className="block mb-2">Occupation *</label>
              <input
                type="text"
                name="occupation"
                value={formData.occupation}
                onChange={handleInputChange}
                placeholder="Your occupation"
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              />
            </div>
            <button
              type="button"
              onClick={handleNext}
              className="w-full bg-indigo-600 py-2 rounded-md text-white hover:bg-indigo-700"
            >
              Next: KYC Info
            </button>
          </>
        )}

        {/* Step 2: KYC Info */}
        {currentStep === 2 && (
          <>
            <div>
              <label className="block mb-2">Annual Income *</label>
              <input
                type="number"
                name="annual_income"
                value={formData.kyc.annual_income}
                onChange={handleInputChange}
                placeholder="Your annual income"
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              />
            </div>
            <div>
              <label className="block mb-2">Employer *</label>
              <input
                type="text"
                name="employer"
                value={formData.kyc.employer}
                onChange={handleInputChange}
                placeholder="Your employer"
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              />
            </div>
            <div>
              <label className="block mb-2">Designation *</label>
              <input
                type="text"
                name="designation"
                value={formData.kyc.designation}
                onChange={handleInputChange}
                placeholder="Your designation"
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              />
            </div>
            <div>
              <label className="block mb-2">Bank Account Statement *</label>
              <input
                type="file"
                name="bank_account_statement"
                onChange={handleFileChange}
                className="block w-full text-sm text-gray-300"
                required
              />
            </div>
            <div>
              <label className="block mb-2">ID Type *</label>
              <select
                name="id_type"
                value={formData.kyc.id_type}
                onChange={handleInputChange}
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              >
                <option value="">Select ID Type</option>
                {idTypes.map((id) => (
                  <option key={id} value={id}>
                    {id}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label className="block mb-2">ID Number *</label>
              <input
                type="text"
                name="id_number"
                value={formData.kyc.id_number}
                onChange={handleInputChange}
                placeholder="ID Number"
                className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
                required
              />
            </div>
            <div>
              <label className="block mb-2">ID Front *</label>
              <input
                type="file"
                name="id_front"
                onChange={handleFileChange}
                className="block w-full text-sm text-gray-300"
                required
              />
            </div>
            {formData.kyc.id_type === "National ID" && (
              <div>
                <label className="block mb-2">ID Back *</label>
                <input
                  type="file"
                  name="id_back"
                  onChange={handleFileChange}
                  className="block w-full text-sm text-gray-300"
                  required
                />
              </div>
            )}
            <div className="flex justify-between">
              <button
                type="button"
                onClick={handleBack}
                className="w-1/3 bg-gray-700 py-2 rounded-md text-white hover:bg-gray-800"
              >
                Back
              </button>
              <button
                type="submit"
                className="w-2/3 bg-indigo-600 py-2 rounded-md text-white hover:bg-indigo-700"
              >
                Submit
              </button>
            </div>
          </>
        )}
      </form>
    </section>
  );
}
