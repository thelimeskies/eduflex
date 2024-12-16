"use client";

import { useState } from "react";

const categoriesList = ["Primary", "Junior Secondary", "Senior Secondary"];

export default function SchoolOnboarding({ onSubmit }: { onSubmit: (data: any) => void }) {
  const [formData, setFormData] = useState({
    name: "",
    address: "",
    phone: "",
    email: "",
    website: "",
    logo: null as File | null,
    categories: [] as string[],
  });

  const [logoPreview, setLogoPreview] = useState<string | null>(null);

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleCheckboxChange = (category: string) => {
    setFormData((prev) => {
      const categories = prev.categories.includes(category)
        ? prev.categories.filter((c) => c !== category)
        : [...prev.categories, category];
      return { ...prev, categories };
    });
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files ? e.target.files[0] : null;
    setFormData({ ...formData, logo: file });

    // Generate preview for the uploaded logo
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setLogoPreview(reader.result as string);
      };
      reader.readAsDataURL(file);
    } else {
      setLogoPreview(null); // Reset preview if no file is selected
    }
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!formData.name || !formData.address || !formData.phone || !formData.email) {
      alert("Please fill in all required fields.");
      return;
    }

    console.log("Form Data Submitted:", formData);
    onSubmit(formData); // Pass form data to parent component
  };

  return (
    <section className="max-w-3xl mx-auto mt-10 bg-gray-800 p-8 rounded-lg shadow-lg text-gray-200">
      <h2 className="text-3xl font-semibold mb-6 text-center">School Onboarding</h2>
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Name */}
        <div>
          <label className="block mb-2">Name *</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            placeholder="School Name"
            className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
            required
          />
        </div>

        {/* Address */}
        <div>
          <label className="block mb-2">Address *</label>
          <textarea
            name="address"
            value={formData.address}
            onChange={handleInputChange}
            placeholder="School Address"
            rows={3}
            className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
            required
          ></textarea>
        </div>

        {/* Phone */}
        <div>
          <label className="block mb-2">Phone *</label>
          <input
            type="text"
            name="phone"
            value={formData.phone}
            onChange={handleInputChange}
            placeholder="School Phone"
            className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
            required
          />
        </div>

        {/* Email */}
        <div>
          <label className="block mb-2">Email *</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            placeholder="School Email"
            className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
            required
          />
        </div>

        {/* Website (Optional) */}
        <div>
          <label className="block mb-2">Website</label>
          <input
            type="url"
            name="website"
            value={formData.website}
            onChange={handleInputChange}
            placeholder="https://example.com"
            className="w-full rounded-md border border-gray-700 bg-gray-900 p-2 text-gray-300"
          />
        </div>

        {/* Logo Upload */}
        <div>
          <label className="block mb-2">School Logo</label>
          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            className="block w-full text-sm text-gray-300"
          />
          {logoPreview && (
            <div className="mt-4">
              <p className="text-sm mb-2">Logo Preview:</p>
              <img
                src={logoPreview}
                alt="Logo Preview"
                className="h-24 w-24 rounded border border-gray-700 object-cover"
              />
            </div>
          )}
        </div>

        {/* Categories (Multi-Select Checkboxes) */}
        <div>
          <label className="block mb-2">Select Categories *</label>
          <div className="flex flex-wrap gap-4">
            {categoriesList.map((category) => (
              <label key={category} className="flex items-center space-x-2">
                <input
                  type="checkbox"
                  checked={formData.categories.includes(category)}
                  onChange={() => handleCheckboxChange(category)}
                  className="h-5 w-5 text-indigo-600"
                />
                <span>{category}</span>
              </label>
            ))}
          </div>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="w-full bg-indigo-600 py-2 rounded-md text-white hover:bg-indigo-700"
        >
          Submit Onboarding
        </button>
      </form>
    </section>
  );
}
