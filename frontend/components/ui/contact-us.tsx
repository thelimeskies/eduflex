"use client";

import { useState } from "react";

export default function ContactUs() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);
  };

  return (
    <section className="relative py-12 bg-gray-900 sm:py-20">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-semibold text-gray-200">Contact Us</h2>
          <p className="mt-4 text-gray-400">
            Have questions? Send us a message and we'll get back to you!
          </p>
        </div>
        <form onSubmit={handleSubmit} className="max-w-2xl mx-auto bg-gray-800 p-8 rounded-lg shadow-lg">
          <div className="mb-6">
            <label htmlFor="name" className="block mb-2 text-gray-300">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              onChange={handleChange}
              className="w-full p-2 rounded-md border border-gray-700 bg-gray-900 text-gray-300"
              placeholder="Your name"
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="email" className="block mb-2 text-gray-300">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              onChange={handleChange}
              className="w-full p-2 rounded-md border border-gray-700 bg-gray-900 text-gray-300"
              placeholder="Your email"
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="message" className="block mb-2 text-gray-300">Message</label>
            <textarea
              id="message"
              name="message"
              onChange={handleChange}
              className="w-full p-2 rounded-md border border-gray-700 bg-gray-900 text-gray-300"
              rows={5}
              placeholder="Write your message"
              required
            ></textarea>
          </div>
          <button
            type="submit"
            className="w-full py-2 px-4 bg-indigo-600 text-white rounded-md hover:bg-indigo-700"
          >
            Send Message
          </button>
        </form>
      </div>
    </section>
  );
}
